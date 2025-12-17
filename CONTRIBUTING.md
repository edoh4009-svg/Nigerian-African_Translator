## 👥 Team Members

| # | Name | Role | Language | Contribution |
|---|------|------|----------|--------------|
| 1 | Momodu Daniel | Contributor | Swahili |  Swahili dictionary |
| 2 | John Bright | Contributor | Yoruba | Yoruba dictionary implementation |
| 3 | Simpa Ibrahim | Contributor | Hausa | Hausa dictionary implementation |
| 4 | Edoh Godwin | Team leader | Zulu | Project management & Zulu dictionary implementation |
| 5 | Kamsi | Contributor | Igbo | Igbo dictionary implementation |

This project was created for **Computer Science 101** at **Bingham University Keffi**
- **Team Lead**: Edoh Godwin - edoh4009@gmail.com
- **Made with ❤️ by Team 5 - The African Translators**
- # Get commit count
echo "GitHub Commits: $(git rev-list --count HEAD)"

# Get number of contributors
echo "Contributors: $(git shortlog -s -n | wc -l)"

# Get project duration
echo "Project Duration: $(git log --reverse --pretty=format:"%ad" --date=short | head -1) - $(date +%Y-%m-%d)"
