# MITRE ATT&CK Info Grabber for Qualys

## Overview

The **MITRE ATT&CK Info Grabber for Qualys** is a specialized cybersecurity tool designed to bridge the gap between Qualys vulnerability management data and the MITRE ATT&CK framework. This tool automatically extracts vulnerability data from Qualys' VMDR (Vulnerability Management, Detection, and Response) platform and maps it to the MITRE ATT&CK matrix, providing security teams with actionable intelligence about their threat landscape.

## What This Tool Does

### Core Functionality
- **Automated Data Extraction**: Connects to Qualys' REST API to pull vulnerability data in real-time
- **MITRE ATT&CK Mapping**: Automatically categorizes vulnerabilities according to the MITRE ATT&CK framework's tactics and techniques
- **Risk Prioritization**: Focuses on high-severity vulnerabilities (Critical, High, and Medium) that are confirmed and actively running
- **Data Aggregation**: Groups vulnerabilities by ATT&CK tactics and techniques, providing count-based analysis
- **Export Capabilities**: Generates structured CSV files for easy analysis and reporting

### Technical Process
1. **API Authentication**: Uses HTTP Basic Authentication to securely connect to Qualys
2. **MITRE Data Sync**: Downloads the latest MITRE ATT&CK Enterprise matrix to ensure up-to-date threat intelligence
3. **Vulnerability Querying**: Executes targeted queries against Qualys' asset vulnerability pivot API
4. **Data Processing**: Filters and processes vulnerability data based on severity, confirmation status, and kernel running state
5. **CSV Generation**: Creates timestamped CSV files with tactic-technique-count relationships

## Use Cases

### Security Operations Teams
- **Threat Hunting**: Identify which ATT&CK techniques are most prevalent in your environment
- **Risk Assessment**: Understand your organization's exposure to specific attack patterns
- **Incident Response**: Prioritize remediation efforts based on ATT&CK framework alignment
- **Compliance Reporting**: Generate reports that align with industry-standard threat frameworks

### Vulnerability Management
- **Trend Analysis**: Track changes in attack technique prevalence over time
- **Resource Allocation**: Focus remediation efforts on the most impactful attack vectors
- **Executive Reporting**: Provide high-level threat landscape summaries to stakeholders

## Project Structure

```
src/
├── main.py                    # Main orchestration script
├── QualysAPIRequest.py        # Handles Qualys API communication and data extraction
├── MitreMatrixUpdate.py       # Manages MITRE ATT&CK matrix updates and data retrieval
├── ExportToEXCEL.py          # Handles CSV data formatting and export
└── requirements.txt           # Python dependencies and versions
```

## Key Features

### Intelligent Rate Limiting
- Built-in retry mechanisms to handle Qualys API rate limiting
- Exponential backoff strategy to prevent API overload
- Graceful error handling for temporary API issues

### Focused Vulnerability Filtering
- **Severity Focus**: Only processes Critical (5), High (4), and Medium (3) severity vulnerabilities
- **Confirmation Status**: Prioritizes confirmed vulnerabilities over potential ones
- **Active Threats**: Filters out vulnerabilities on non-running kernels to focus on active threats

### MITRE ATT&CK Coverage
- Covers 9 key ATT&CK tactics:
  - Initial Access
  - Execution
  - Persistence
  - Privilege Escalation
  - Defense Evasion
  - Credential Access
  - Lateral Movement
  - Collection
  - Impact

### Automated Data Management
- Self-updating MITRE ATT&CK matrix from official sources
- Timestamped output files for historical tracking
- Structured logging for audit and debugging purposes

## Setup and Installation

### Prerequisites
- Python 3.7+ with pip package management
- Valid Qualys API credentials with VMDR access
- Network access to Qualys API endpoints

### Installation Options

#### Option 1: Executable (Windows)
1. Download the latest [release](https://github.com/dakotaPPP/MITRE-ATTACK-Info-Grabber-for-Qualys/releases/)
2. **Important**: Place the .exe in its own dedicated folder
3. The program will create necessary directories and configuration files automatically

#### Option 2: Source Code
1. Clone or download the source code
2. Install dependencies: `pip install -r src/requirements.txt`
3. Run the main script: `python src/main.py`

### Configuration
1. The tool automatically creates a `config/config.json` file on first run
2. Update the configuration with your Qualys credentials:
   ```json
   {
     "username": "your_qualys_username",
     "password": "your_qualys_password",
     "base_url": "https://your_qualys_instance.qualys.com"
   }
   ```

## Output and Analysis

### Generated Files
- **CSV Files**: Located in `/logs/CSVs/` with naming format: `tactic_technique_counts_YYYY-MM-DDThh-mm-ss.csv`
- **Data Logs**: Comprehensive logs in `/logs/data_log.txt` for debugging and audit purposes

### CSV Structure
The generated CSV contains three columns:
- **Tactic**: The MITRE ATT&CK tactic (e.g., "Initial Access", "Execution")
- **Technique**: The specific ATT&CK technique (e.g., "T1566.001", "T1059.001")
- **Count**: Number of vulnerabilities associated with that technique

### Data Visualization
1. Open the CSV in Excel or similar spreadsheet application
2. Select all data (including headers)
3. Insert → PivotTable
4. Configure the pivot table fields for your analysis needs

## Technical Requirements

### Python Dependencies
- **Core Libraries**: requests, json, csv, datetime
- **MITRE Integration**: mitreattack-python for ATT&CK framework processing
- **Data Processing**: Additional utilities for robust error handling and data manipulation

### API Requirements
- Qualys VMDR API access
- HTTP Basic Authentication support
- Asset vulnerability pivot endpoint access

## Security Considerations

- **Credential Storage**: API credentials are stored locally in JSON format
- **Network Security**: Ensure secure network access to Qualys API endpoints
- **Data Handling**: Generated files contain vulnerability information - handle according to your organization's data classification policies

## Troubleshooting

### Common Issues
- **Configuration Errors**: Ensure config.json contains valid Qualys credentials
- **API Rate Limiting**: The tool includes automatic retry logic, but may need adjustment for high-volume environments
- **Network Connectivity**: Verify firewall rules allow access to Qualys API endpoints

### Log Analysis
- Check `/logs/data_log.txt` for detailed execution information
- Review console output for real-time status updates
- Verify CSV generation in the `/logs/CSVs/` directory

## Contributing

This project was created at the request of Larry Lotspeich, Threat and Vulnerability Management Manager at Entergy. Contributions and improvements are welcome to enhance the tool's functionality and usability.

## License

This project is licensed under the terms specified in the LICENSE file.

---

**Note**: This tool is designed for security professionals and requires appropriate Qualys API access. Always ensure you have proper authorization before running vulnerability assessment tools in your environment.
