import xlrd
import csv
from decimal import Decimal
import os
os.makedirs("output", exist_ok=True)

from relab_preprocess_vars import (
    material_classes, meteorites, sediments, organics, minerals, rocks, 
    synthetics, minerals_o, mixtures_o, organics_o, rocks_o, sediments_o
)

sample_cat_dir = "../RelabDatabase2024Dec31/catalogues/Sample_Catalogue.xls"
spectra_cat_dir = "../RelabDatabase2024Dec31/catalogues/Spectra_Catalogue.xls"
chem_analyses_dir = "../RelabDatabase2024Dec31/catalogues/Chem_Analyses.xls"
data_dir = "../RelabDatabase2024Dec31/data/"


# classifies the sample type of sample based on metadata
# changed to "Sample type" -- VISOR has additonal field for "Material class" but Sample type is used for consistency
def get_sample_type(id, source, genType1, gen_type_2, type1, type2, subtype):

    # hard coded id classifications
    match id:
        case 'DH-CMP-026': return 'Reference'
        case 'DH-CMP-027': return 'Rock'
        case 'DH-CMP-028': return 'Rock'
        case 'SS-CMP-001': return 'Rock'
        case 'SS-CMP-002': return 'Rock'
        case 'SS-CMP-003': return 'Rock'
        case 'SS-CMP-004': return 'Rock'
        case 'TT-CMP-001': return 'Synthetic'
    
    if 'sediment' in genType1.lower(): return 'Mixture'
    if 'standard' in type1.lower(): return 'Reference'
    if 'synthetic' in source.lower(): return 'Synthetic'
    if 'biological' in genType1.lower(): return 'Organic'
        
    if source in meteorites: return 'Meteorites'

    if 'moon-ret' in source.lower(): return 'Returned Planetary Samples'
    if 'mixture' in type1.lower(): return 'Mixture'
    if 'dune sand' in type1.lower(): return 'Sediment'

    if genType1 in material_classes: return genType1

    if 'mixture' in gen_type_2.lower(): return 'Mixture'
    
    if genType1 in sediments: return 'Sediment'
    if genType1 in organics: return 'Organic'
    if genType1 in minerals: return 'Mineral'
    if genType1 in rocks: return 'Rock'
    if genType1 in synthetics: return 'Synthetic'

    if 'quartz kbr' in subtype.lower(): return 'Rock'

    # outlier (hard coded) classifications
    sample_attributes = f'{genType1}, {type1}, {subtype}'
    if sample_attributes in minerals_o: return 'Mineral'
    if sample_attributes in mixtures_o: return 'Mixture'
    if sample_attributes in organics_o: return 'Organic'
    if sample_attributes in rocks_o: return 'Rock'
    if sample_attributes in sediments_o: return 'Sediment'

    # default case
    return None


def load_sample_data():
    # read sample category excel file
    sample_cat = xlrd.open_workbook(sample_cat_dir).sheet_by_index(0)
    
    sample_data = {}
    
    # apply algorithm to all samples, store metadata
    for sample in range(1, sample_cat.nrows):

        # retrieve sample metadata
        sample_id      = sample_cat.cell_value(rowx=sample, colx=0)
        sample_name    = sample_cat.cell_value(rowx=sample, colx=1)
        source         = sample_cat.cell_value(rowx=sample, colx=5)
        gen_type_1     = sample_cat.cell_value(rowx=sample, colx=6)
        gen_type_2     = sample_cat.cell_value(rowx=sample, colx=7)
        type_1         = sample_cat.cell_value(rowx=sample, colx=8)
        type_2         = sample_cat.cell_value(rowx=sample, colx=9)
        sub_type       = sample_cat.cell_value(rowx=sample, colx=10)
        min_grain_size = sample_cat.cell_value(rowx=sample, colx=12)
        max_grain_size = sample_cat.cell_value(rowx=sample, colx=13)
        origin         = sample_cat.cell_value(rowx=sample, colx=16)
        # location       = sample_cat.cell_value(rowx=sample, colx=17)
        location       = 'RELAB' # Changed from ReLab
        chem_num       = sample_cat.cell_value(rowx=sample, colx=18)
        text           = sample_cat.cell_value(rowx=sample, colx=19)

        # classify sample type
        s_type = get_sample_type(sample_id, source, gen_type_1, gen_type_2, type_1, type_2, sub_type)

        if s_type:
            sample_data[sample_id] = {
                "chem_number": str(int(chem_num)) if chem_num != "" else "",
                "max_grain_size": str(max_grain_size),
                "min_grain_size": str(min_grain_size),
                "Location": location,
                "sample_name": sample_name,
                "MaterialClass": gen_type_1,
                "SampleType": s_type,
                "SubType": sub_type,
                "Origin": origin,
                "SampleDescription": text
            }
        
        else:
            sample_str = f'{gen_type_1}, {type_1}, {sub_type}'
            print(f'Skipping {sample_str}. Could not classify.')
    
    print("")
    return sample_data


def load_chem_analysis():
    chemCat = xlrd.open_workbook(chem_analyses_dir).sheet_by_index(0)

    chem_analysis = {}

    # store relevant data from chem catalogue under reference number 
    for val in range(1, chemCat.nrows):
        
        ref_num = str(int(chemCat.cell_value(rowx=val, colx=0)))
        other_info = str(chemCat.cell_value(rowx=val, colx=22)).strip()
        references = str(chemCat.cell_value(rowx=val, colx=21)).strip()

        chem_analysis[ref_num] = {"OtherInfo": other_info, "References": references}
    
    return chem_analysis


if __name__ == "__main__":
    
    output_cnt = 0
    error_log_path = "ingest_error_log.txt"
    with open(error_log_path, "w", encoding="utf-8") as error_log:
        
        sample_data = load_sample_data()
        chem_analysis = load_chem_analysis()
        
        spectra_cat = xlrd.open_workbook(spectra_cat_dir).sheet_by_index(0)
        
        # get relevant data from specta catalogue under sample_id 
        for spectra in range(1, spectra_cat.nrows):
            
            spectra_data = {}

            # get spectra info
            spectra_id = spectra_cat.cell_value(rowx=spectra, colx=0)
            min_wavelength = int(spectra_cat.cell_value(rowx=spectra, colx=5))
            max_wavelength = int(spectra_cat.cell_value(rowx=spectra, colx=6))
            resolution = spectra_cat.cell_value(rowx=spectra, colx=7)
            date_added = spectra_cat.cell_value(rowx=spectra, colx=2)
            source_angle = spectra_cat.cell_value(rowx=spectra, colx=8)
            detect_angle = spectra_cat.cell_value(rowx=spectra, colx=9)
            reference = spectra_cat.cell_value(rowx=spectra, colx=22)
            
            date_added = xlrd.xldate_as_datetime(date_added, 1).date().isoformat()
            view_geo = f'{source_angle}° / {detect_angle}°' if (source_angle!="NA" and detect_angle!="NA") else "Unknown"

            # get sample info
            sample_id = spectra_cat.cell_value(rowx=spectra, colx=1)
            
            try:
                spectra_sample_data = sample_data[sample_id]
            except Exception as e:
                # skip spectra whose id is not classified
                error_log.write(f'Could not find sample data for {sample_id} (row {spectra}): {e}\n')
                continue
            
            # skip spectra whose sample type was not classified
            if (spectra_sample_data['SampleType'] == ''): continue

            # get chem analysis info
            sub_type_info = spectra_sample_data["SubType"]
            chem_num = spectra_sample_data["chem_number"]
            other_info = chem_analysis[chem_num]["OtherInfo"] if (chem_num!="0" and chem_num!='') else ""
            refs = chem_analysis[chem_num]["References"] if (chem_num!="0" and chem_num!='') else ""

            # prepare grain size metadata
            grain_size = 'Unknown'
            min_grain = spectra_sample_data["min_grain_size"]
            max_grain = spectra_sample_data["max_grain_size"]
            sample_name = spectra_sample_data["sample_name"]
            name_lower = str(sample_name).lower()
            keywords = ["chip", "slab", "rock", "cube"]
            try:
                min_val = float(min_grain)
                max_val = float(max_grain)
                if any(keyword in name_lower for keyword in keywords):
                    grain_size = "Whole Object"
                elif min_val == 0.0 and max_val == 0.0:
                    grain_size = "Unknown"
                elif min_val > 0.0 and (max_val == 0.0 or max_grain == ""):
                    grain_size = str(min_val)
                elif max_val > 0.0 and min_grain == "": # range can be from 0 to max
                    grain_size = str(max_val)
                else:
                    grain_size = f"({min_val} - {max_val})" # default case, min - max
            except ValueError as e:
                if any(keyword in name_lower for keyword in keywords):
                    grain_size = "Whole Object"
                else:
                    grain_size = "Unknown"

            #composite header strings
            other_info_str = ""
            other_info = other_info or ""
            sub_type_info = sub_type_info or ""
            if other_info != "":
                other_info_str += other_info
            if other_info != "" and sub_type_info != "":
                other_info_str += ", "
            if sub_type_info != "":
                other_info_str += sub_type_info

            ref_str = ""
            refs = refs or ""
            reference = reference or ""
            if refs != "":
                ref_str += refs
            if refs != "" and reference != "":
                ref_str += ", "
            if reference != "":
                ref_str += reference

            # prepare header
            header = [
                ["Composition", ""],
                ["Date Added", date_added or ""],
                ["Formula", ""],
                ["Grain Size Description", f'<{spectra_sample_data["max_grain_size"]}um' or ""],
                ["Grain Size", grain_size or ""],
                ["Locality", spectra_sample_data["Origin"] or ""],
                ["Minimum Wavelength", min_wavelength or ""],
                ["Sample Name", spectra_sample_data["sample_name"] or ""],
                ["Maximum Wavelength", max_wavelength or ""],
                ["Database of Origin", spectra_sample_data["Location"] or ""],
                ["Other Information", other_info_str or ""],
                ["References", ref_str or ""],
                ["Resolution", resolution or ""],
                ["Material class", spectra_sample_data["SampleType"] or ""],
                ["Sample Description", spectra_sample_data["SampleDescription"] or ""],
                ["Sample ID", spectra_id or ""],
                ["Original Sample ID", sample_id or ""],
                ["Viewing Geometry", view_geo or ""],
                ["Wavelength", "Response"] # Wavelength must go at end of header; used by split_data_and_metadata function during ingest
            ]
            
            # compute location of spectral data
            pi_initials = sample_id.split("-")[1].lower()
            sub_folder_name = sample_id.split("-")[0].lower()
            file_path = f'{data_dir}{pi_initials}/{sub_folder_name}/{spectra_id.lower()}.txt'
            
            try:
                # read spectral data
                lines = open(file_path).read().splitlines()
                lines = lines[2:] # remove first two lines
            except Exception as e:
                print(f'Could not find directory {file_path}')
                error_log.write(f'Could not find directory {file_path} (row {spectra}): {e}\n')
                continue

            try:
                # convert data from microns to nms
                MICRON_TO_NM = 1000
                data = [
                    [
                        str(float(Decimal(line.split("\t")[0]) * MICRON_TO_NM )),
                        str(float(Decimal(line.split("\t")[1]))) # <-- Reflectance should be 0..1 (not multiplied by 1000)
                    ]
                    for line in lines
                ]
            except Exception as e:
                print(f'Error parsing data at {file_path}')
                error_log.write(f'Error parsing data at {file_path} (row {spectra}): {e}\n')
                continue

            output_dest = f'output/{sub_folder_name}_{pi_initials}_{spectra_id.lower()}.csv'
            try:
                with open(output_dest, 'w', newline='', encoding="utf-8") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerows(header)
                    writer.writerows(data)
                print(f'Successfully wrote {output_dest}')
                output_cnt+=1
            except Exception as e:
                error_log.write(f'Error writing CSV {output_dest} (row {spectra}): {e}\n')
                
    print("")
    print(f'Wrote {output_cnt} files.')
    print(f'Errors logged to {error_log_path}')
