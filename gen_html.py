import os
import json

WAVS_ROOT = 'resources/bahnar'
file_map = json.load(open(os.path.join(WAVS_ROOT, "file_map.json")))
rawfile_map = json.load(open(os.path.join(WAVS_ROOT, "rawfile_map.json")))
file_text = json.load(open(os.path.join(WAVS_ROOT, "file_text.json")))

template="""
        <tr>
            <td colspan='5'>{text}</td>
            </tr>
        <tr>
            <th scope="row">wav</th>
            <td><audio controls="" ><source src="{file1}" type="audio/wav"></audio></td>
            <td><audio controls="" ><source src="{file2}" type="audio/wav"></audio></td>
            <td><audio controls="" ><source src="{file3}" type="audio/wav"></audio></td>
            <td><audio controls="" ><source src="{file4}" type="audio/wav"></audio></td>
            </tr>
        """
        
choosen_gt_files = list(file_map.keys())[:5]

folders = ['scratch_400', 'ph_no_pr_400', 'our_400']

our_table = []
for f in choosen_gt_files:
    text = file_text[f]
    file1= os.path.join(WAVS_ROOT, 'GT', f)
    file2= os.path.join(WAVS_ROOT, folders[0], rawfile_map[f])
    file3= os.path.join(WAVS_ROOT, folders[1], file_map[f])
    file4= os.path.join(WAVS_ROOT, folders[2], file_map[f])
    our_table.append(template.format(text=text, file1=file1, file2=file2, file3=file3, file4=file4))
    
print(''.join(our_table))