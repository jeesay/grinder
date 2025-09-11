import re

def extract_parameters_from_cpp(cpp_code):
    results = []

    # Match addParams("Label", default, "Help text")
    add_params_pattern = re.compile(
        r'addParams?\s*\(\s*"([^"]+)"\s*,\s*([^\s,]+)\s*,\s*"([^"]+)"\s*\)', re.MULTILINE
    )

    # Match parser->addOption("cli_arg", &var, "Help text", default_val)
    add_option_pattern = re.compile(
        r'addOption\s*\(\s*"([^"]+)"\s*,\s*&?(\w+)\s*,\s*"([^"]+)"(?:\s*,\s*([^\)]+))?', re.MULTILINE
    )

    # Extract GUI params
    for match in add_params_pattern.findall(cpp_code):
        label, default, help_text = match
        # Try to guess widget type from label or default
        if 'fn_' in default or 'file' in label.lower():
            widget = 'file widget'
        elif default.isdigit():
            widget = 'slider'
        else:
            widget = 'text widget'
        results.append([label, widget, default, help_text, ''])

    # Extract CLI options
    for match in add_option_pattern.findall(cpp_code):
        cli_arg, var_name, help_text, default = match
        results.append(["", "CLI Option", default.strip() if default else "", help_text, cli_arg])

    return results


# Example usage:
with open("./pipeline_jobs.cpp", "r", encoding="utf-8") as f:
    cpp_code = f.read()

params_table = extract_parameters_from_cpp(cpp_code)

# Display as Markdown
markdown_table = "| GUI Label | Widget Type | Default Value | Help Text | CLI Argument |\n"
markdown_table += "|-----------|-------------|----------------|-----------|---------------|\n"
for row in params_table:
    markdown_table += "| " + " | ".join(row) + " |\n"

markdown_table[:3000]  # Preview first rows

