# Biomancy

PowerBI Operations client library for Python -- The Animation of Business Intelligence Operations

## Motivation

PowerBI is a powerful business intelligence tool, but its capabilities are often constrained by its graphical interface and limited programmability. Biomancy was born out of frustration with these limitations. As data professionals, we found ourselves repeatedly performing the same manual tasks in PowerBI - adjusting visual properties across multiple reports, migrating configurations between environments, and documenting report structures. These tasks are tedious, error-prone, and time-consuming when performed through the PowerBI interface.

The name "Biomancy" - derived from "bio" (life) and "mancy" (divination) - reflects our mission to breathe life into PowerBI operations through code. Just as a biomancer would animate the inanimate, our library animates the static structures of PowerBI, allowing them to be manipulated, analyzed, and transformed programmatically.

## Introduction

Biomancy is a Python client library that provides programmatic access to PowerBI report structures, visual elements, and configurations. It allows developers, data engineers, and PowerBI administrators to interact with PowerBI at a fundamental level, enabling automation, analysis, and transformation of reports beyond what is possible through the standard PowerBI interface.

The library parses and represents PowerBI Desktop project files (PBIP), making their structure accessible via a clean, Pythonic API. This enables automated processing of reports, consistent formatting across visuals, detailed documentation generation, and much more.

## Features

- **Report Structure Access**: Navigate through pages, visuals, and groups in PowerBI reports
- **Component Properties**: Access and analyze visual properties, positions, and configurations
- **Theme Management**: Work with PowerBI themes and color definitions
- **Metadata Extraction**: Extract and analyze report metadata
- **Custom Visual Support**: Work with both standard and custom visuals

## Installation

```bash
pip install biomancy
```

## Quick Start

```python
from biomancy import Report

# Load a PowerBI report from a PBIP directory
report = Report("path/to/report.pbip")

# Access pages
for page in report.pages:
    print(f"Page: {page.display_name}")
    
    # Access visuals on each page
    for visual in page.visuals:
        print(f"  Visual: {visual.name}, Type: {visual.type}")
        print(f"  Position: x={visual.x}, y={visual.y}, width={visual.width}, height={visual.height}")

# Get all visuals of a specific type
charts = report.get_all_visuals_of_type("lineChart")
for chart in charts:
    print(f"Line Chart: {chart.name}")
```

## Use Cases

### Report Auditing and Documentation

Generate comprehensive documentation of your PowerBI reports, including inventory of visuals, data sources, and relationships.

```python
import pandas as pd
from biomancy import Report

report = Report("path/to/report.pbip")

# Create a visual inventory
visual_data = []
for page in report.pages:
    for visual in page.visuals:
        visual_data.append({
            "page": page.display_name,
            "visual_name": visual.name,
            "visual_type": visual.type,
            "width": visual.width,
            "height": visual.height,
            "x": visual.x,
            "y": visual.y
        })

# Convert to DataFrame for analysis or export
visual_inventory = pd.DataFrame(visual_data)
visual_inventory.to_csv("report_inventory.csv")
```

### Bulk Visual Formatting

Apply consistent formatting to all visuals of a specific type across a report.

### Report Migration and Transformation

Automate the migration of reports between environments with appropriate transformations.

### Compliance Checking

Verify that reports meet organizational standards for formatting, accessibility, and security.

## PowerBI Pain Points and Limitations

PowerBI, while powerful in its visualization capabilities, presents several challenges for organizations seeking to standardize, automate, and scale their business intelligence operations:

1. **Limited Programmatic Access**: PowerBI's API offerings primarily focus on service operations rather than report structure manipulation.

2. **Manual Repetitive Tasks**: Formatting, layout adjustments, and visual configuration often require repetitive manual work, especially across multiple reports.

3. **Environment Migration Challenges**: Moving reports between development, testing, and production environments often requires manual reconfiguration.

4. **Governance at Scale**: Enforcing consistent standards across hundreds or thousands of reports is nearly impossible without programmatic tools.

5. **Documentation Overhead**: Creating and maintaining documentation for complex reports is time-consuming and quickly becomes outdated.

6. **Version Control Limitations**: While PBIP files are more amenable to version control than PBIX, working with these formats still presents challenges.

7. **Customization Barriers**: Implementing organization-specific requirements or extending functionality beyond built-in capabilities requires workarounds.

Existing tools in the ecosystem primarily focus on data connections and refreshes, rather than addressing these operational challenges. PowerBI developers often resort to manual processes or fragile automation scripts that interact with the PowerBI interface, leading to brittle solutions that break with UI changes.

Biomancy addresses these gaps by providing a clean, Pythonic interface to the underlying structures of PowerBI reports, enabling true automation and programmatic control.

## Future Directions

Biomancy is under active development, with several exciting features on the roadmap:

- **Write Support**: Enable modifications to report structures and visual properties
- **Theme Creation**: Programmatically generate and apply themes
- **Report Generation**: Create reports from templates and data
- **CI/CD Integration**: First-class support for PowerBI in CI/CD pipelines
- **Comparison Tools**: Diff and merge capabilities for report versions
- **Extended Visual Support**: Support for more complex visual types and custom visuals

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The PowerBI community for sharing knowledge about report structures
- The Python community for inspiration in API design
- All contributors who have helped shape this project
