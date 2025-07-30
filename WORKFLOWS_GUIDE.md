# GitHub Workflows for Project Template Generation

This repository has three GitHub Actions workflows configured for creating project templates from files in the `files/` folder.

## 🚀 Available Workflows

### 1. **Quick Template Download** (`quick-template.yml`) 
Quick template creation for immediate download.

**How to use:**
1. Go to `Actions` → `Quick Template Download`  
2. Click `Run workflow`
3. Choose whether to include altlib libraries
4. Download archive from Artifacts section

**Result:** Artifact available for download for 7 days

### 2. **Custom Template Builder** (`custom-template.yml`)
Advanced template builder with customization options.

**How to use:**
1. Go to `Actions` → `Custom Template Builder`
2. Click `Run workflow`
3. Configure parameters:
   - **Project name** - project name (optional)
   - **Include altlib** - include component libraries
   - **Include workflows** - include GitHub Actions
   - **Include docs** - include documentation
   - **Template format** - archive format (ZIP/TAR.GZ/both)

**Result:** Customized template in Artifacts

## 📁 What's included in the template

### Core files (always):
- `PCB.PcbDoc` - Altium PCB template file
- `Job.OutJob` - Output settings
- `board_options.txt` - Board manufacturing options  
- `ext_bom.csv` - External BOM template
- `.gitignore` - Git settings
- `README.md` - Documentation template

### Optional components:
- `altlib/` - RHS component libraries
- `.github/workflows/` - CI/CD workflows
- `PROJECT_SETUP_GUIDE.md` - Detailed setup guide

## 🔧 How to run workflows

### Via GitHub web interface:
1. Open repository on GitHub
2. Go to `Actions` tab
3. Select needed workflow from the left list
4. Click `Run workflow` button
5. Fill parameters and run

### Via GitHub CLI:
```bash
# Quick template
gh workflow run quick-template.yml

# Custom template with parameters
gh workflow run custom-template.yml \
  -f project_name="MyProject" \
  -f include_altlib=true \
  -f template_format="zip"

## 📦 Downloading results

### From Artifacts:
1. Open completed workflow run
2. Scroll down to "Artifacts" section
3. Download needed archive

### From Releases:
1. Go to `Releases` tab
2. Find needed template version
3. Download archive from Assets section

## 💡 Usage tips

1. **For development** - use `Quick Template Download`
2. **For distribution** - use `Create Project Template` 
3. **For special needs** - use `Custom Template Builder`

## 🔄 Automatic updates

Workflows automatically:
- Copy current files from `files/`
- Include current version of `altlib/` libraries
- Generate correct documentation
- Create archives in needed format

## 🐛 Troubleshooting

If workflow fails:
1. Check execution logs in Actions
2. Ensure all files in `files/` are correct
3. Check repository access permissions

For questions create an Issue in this repository.
