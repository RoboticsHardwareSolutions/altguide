# Template Generation Workflows Guide

This repository contains automated workflows for generating project templates. The workflows use GitHub Actions with self-hosted runners for local storage and optimal performance.

## 🚀 Available Workflows

### 1. Quick Template Generation (`quick-template.yml`)
**Purpose:** Fast template creation with minimal configuration  
**Trigger:** Manual (workflow_dispatch)  
**Performance:** Optimized for speed using sparse checkout

**Parameters:**
- `template_name` (required): Name for your template output

**What it includes:**
- All files from `files/` directory
- Project documentation (`altguide.md`)
- Creates both ZIP and TAR.GZ formats

### 2. Custom Template Generation (`custom-template.yml`)  
**Purpose:** Advanced template builder with customization options  
**Trigger:** Manual (workflow_dispatch)  
**Performance:** Configurable with conditional file inclusion

**Parameters:**
- `template_name` (required): Name for your template output
- `project_name` (optional): Custom project name for template
- `project_type` (optional): Project type selection (electronics/software/mixed)
- `include_workflows` (optional): Include workflow files (default: false)
- `include_docs` (optional): Include documentation (default: true)
- `template_format` (optional): Output format (zip/tar.gz/both, default: both)

## 📂 Local Storage System

Both workflows now use local storage in the workspace directory:

- **Storage Location:** `./template-storage/` (relative to workspace root)
- **File Permissions:** 644 (readable by all users)
- **Retention:** Managed locally within the workspace

**Advantages:**
- ⚡ Faster access to generated templates
- 💾 No GitHub storage quota limitations
- 🔧 Better control over file management
- 🏃‍♂️ Accessible from workspace directory
- 🔒 No special permissions required

## 📁 What's included in templates

### Core files (always included):
- `PCB.PcbDoc` - Altium PCB template file
- `Job.OutJob` - Output job settings
- `board_options.txt` - Board manufacturing options  
- `ext_bom.csv` - External BOM template
- `altguide-check.yml` - GitHub Actions workflow

### Optional components (custom template only):
- `.github/workflows/` - Additional CI/CD workflows
- Documentation files and guides

## 🔧 How to run workflows

### Via GitHub web interface:
1. Open repository on GitHub
2. Go to `Actions` tab
3. Select workflow from the left panel:
   - `Quick Template Generation` - for fast standard templates
   - `Custom Template Generation` - for customized templates
4. Click `Run workflow` button
5. Fill in required parameters:
   - **Template name**: Choose a descriptive name for your template
   - **Additional options**: Configure as needed (custom workflow only)
6. Click `Run workflow` to start

### Via GitHub CLI:
```bash
# Quick template
gh workflow run quick-template.yml \
  -f template_name="MyProject-Template"

# Custom template with parameters
gh workflow run custom-template.yml \
  -f template_name="MyProject-Custom" \
  -f project_name="MyProject" \
  -f project_type="electronics" \
  -f include_workflows=true \
  -f template_format="zip"
```

## 📦 Accessing generated templates

Templates are stored locally in the workspace:

**File Location:** `./template-storage/[template-name].[format]`

**Available Formats:**
- `[template-name].zip` - ZIP archive format
- `[template-name].tar.gz` - TAR.GZ archive format

The workflow summary will display the exact file paths where templates are saved.

## ⚡ Performance Notes

**Optimization features:**
- 🚀 **Sparse checkout**: Only downloads needed files (`files/` directory and documentation)
- ⚡ **Shallow clone**: Uses `fetch-depth: 1` for faster downloads
- 🏃‍♂️ **Self-hosted runners**: Local execution for better performance
- � **Local storage**: Direct file system access without upload overhead

**Build times:**
- � **Quick template**: ~30-60 seconds
- 🎛️ **Custom template**: ~1-2 minutes (depending on options)

## 💡 Usage recommendations

1. **For rapid prototyping**: Use `Quick Template Generation`
2. **For specific project needs**: Use `Custom Template Generation` with appropriate options
3. **For team distribution**: Generate templates with descriptive names including version or date

## 🔄 Template contents

Workflows automatically:
- Copy all current files from `files/` directory
- Include current project documentation
- Generate templates in requested format(s)
- Store templates locally for immediate access
- Use optimized sparse checkout for faster performance

## 🐛 Troubleshooting

**If workflow fails:**
1. Check execution logs in the Actions tab
2. Verify all files in `files/` directory are accessible
3. Ensure self-hosted runner has sufficient disk space
4. Check runner permissions for `/home/runner/template-storage/`

**Common issues:**
- **Storage space**: Clean up old templates from `./template-storage/`
- **Permissions**: Ensure runner can write to workspace directory
- **Network**: Verify repository access for sparse checkout

For questions or issues, please create an Issue in this repository.

## 📝 Local template creation

For local development, you can also use the Python script:

```bash
# Create template locally
python create_template.py --name "MyTemplate" --type electronics

# Or use the wrapper script
./create_template_wrapper.sh
```

This provides the same functionality as the workflows but runs entirely on your local machine.
