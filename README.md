# Qualys-MITRE-ATTACK-Grabber
 Pulls data from Qualys' API and is grouped by the MITRE ATT&CK matrix. Creates a csv file that allows for easy data visualization via a pivot table.<br />
 Created per Larry Lotspeich's, Threat and Vulnerability Management Manager at Entergy, request.

# Setup
1. Download the latest release package or just download the source code! <br />
**NOTE:** If running via the .exe provided be sure to place this .exe in it's own folder as the program populates and reads from it's own directories <br />
    **NOTE:** If running via the source code, be sure to download all packages used (for quick install of all packages download the `requirements.txt` in the `src` folder) 
2. After program finishes a csv should populate in the directory `/logs/CSVs` <br />
   The CSV naming format is `tactic_technique_counts_YYYY-MM-DDThh-mm-ss.csv`
3. Follow the steps below to create the pivot table <br />
   `Open the CSV in excel -> Select all the data (header included) -> (Insert tab -> PivotTable) -> Select where you want the table -> Check mark all the PivotTable Fields`

Pretty straight forward thank you :D