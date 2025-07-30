# RHS Altguide

Guidelines and templates for PCB project development in Altium Designer by RoboticsHardwareSolutions.

## 🚀 Quick Start - Get Project Template

### Via GitHub Actions (recommended)

1. **Quick template creation:**
   - Go to [Actions](../../actions) → `Quick Template Download`
   - Click `Run workflow`
   - Download the ready archive from Artifacts

2. **Create versioned release:**
   - Go to [Actions](../../actions) → `Create Project Template`
   - Specify version (e.g., `v1.0.0`)
   - Get release with template archives

3. **Custom template:**
   - Go to [Actions](../../actions) → `Custom Template Builder`
   - Configure parameters for your needs
   - Download personalized template

### Locally (for development)

```bash
# Clone the repository
git clone https://github.com/RoboticsHardwareSolutions/altguide.git
cd altguide

# Create template locally
./create_template_local.sh "MyProject" true
```

## 📁 What's included in the template

- **PCB.PcbDoc** - Altium Designer PCB template file
- **Job.OutJob** - Production file output settings
- **board_options.txt** - Board manufacturing specifications
- **ext_bom.csv** - External BOM (Bill of Materials) template
- **.github/workflows/** - GitHub Actions for automatic checks
- **altlib/** - RHS component libraries (optional)
- **Documentation** - Setup and usage guides

## 📚 Documentation

- **[WORKFLOWS_GUIDE.md](WORKFLOWS_GUIDE.md)** - Detailed GitHub Actions guide
- **[altguide.md](altguide.md)** - Main PCB development guide
- **[CHANGELOG.md](CHANGELOG.md)** - Change history

## 🛠 Project Structure

```
altguide/
├── .github/workflows/          # GitHub Actions for template creation
├── files/                      # Project template files
│   ├── PCB.PcbDoc             # PCB template
│   ├── Job.OutJob             # Output settings
│   ├── .github/workflows/     # CI/CD for projects
│   └── ...
├── altlib/                     # RHS component libraries
│   ├── schlibs/               # Schematic libraries
│   ├── pcblibs/               # PCB libraries  
│   ├── snippets/              # Ready-made circuit solutions
│   └── ...
├── utils/                      # Utilities and scripts
└── docs/                       # Additional documentation
```

## 🔧 Tools and Utilities

### Project Verification
- **pcb_checker** - Automatic PCB project verification
- **pcb_specgen** - Specification generation

### GitHub Actions
- **Quick Template** - Fast template creation
- **Custom Template** - Configurable template  
- **Release Template** - Versioned releases

## 🎯 Who is this project for

- **RHS Engineers** - Standardized templates and libraries
- **External Developers** - Ready solutions and best practices
- **Students and Teachers** - Educational materials for PCB design

## 🤝 Contributing

1. Fork this repository
2. Create a branch for your feature (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📋 Requirements

- **Altium Designer** (any modern version)
- **Git** for version control
- **Python 3.11+** for verification scripts (optional)

## 📞 Support

- **Issues** - For questions and suggestions create an [Issue](../../issues)
- **Discussions** - Discussions in [Discussions](../../discussions)
- **Wiki** - Additional documentation in [Wiki](../../wiki)

## 📄 License

This project is distributed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**RoboticsHardwareSolutions** © 2025
