#!/usr/bin/env bash
set -euo pipefail

# Usage:
#   bash scripts/split_portfolio_projects.sh <github-owner>
#
# Example:
#   bash scripts/split_portfolio_projects.sh sky-brazil

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <github-owner>"
  exit 1
fi

OWNER="$1"
ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
WORK_DIR="${ROOT_DIR}/.tmp-separated-repos"

declare -A PROJECT_MAP=(
  ["portfolio-projects/01-lead-enrichment-automation"]="lead-enrichment-automation"
  ["portfolio-projects/02-price-monitoring-api"]="price-monitoring-api"
  ["portfolio-projects/03-job-intelligence-dashboard"]="job-intelligence-dashboard"
)

echo "[INFO] Preparing temporary workspace at: ${WORK_DIR}"
rm -rf "${WORK_DIR}"
mkdir -p "${WORK_DIR}"

for project_path in "${!PROJECT_MAP[@]}"; do
  repo_name="${PROJECT_MAP[$project_path]}"
  src_dir="${ROOT_DIR}/${project_path}"
  dst_dir="${WORK_DIR}/${repo_name}"

  echo "[INFO] Processing ${repo_name}..."
  mkdir -p "${dst_dir}"
  cp -R "${src_dir}/." "${dst_dir}/"

  if [[ ! -f "${dst_dir}/README.md" ]]; then
    echo "[ERROR] README.md missing in ${repo_name}"
    exit 1
  fi

  if [[ ! -f "${dst_dir}/LICENSE" ]]; then
    cp "${ROOT_DIR}/LICENSE" "${dst_dir}/LICENSE"
  fi

  if [[ ! -f "${dst_dir}/.gitignore" ]]; then
    cat > "${dst_dir}/.gitignore" <<'EOF'
.venv/
__pycache__/
*.pyc
*.pyo
*.pyd
*.log
.DS_Store
.pytest_cache/
.mypy_cache/
EOF
  fi

  (
    cd "${dst_dir}"
    git init
    git add .
    git commit -m "chore: initial project import"

    if gh repo view "${OWNER}/${repo_name}" >/dev/null 2>&1; then
      echo "[WARN] ${OWNER}/${repo_name} already exists. Skipping creation."
    else
      gh repo create "${OWNER}/${repo_name}" --public --source=. --remote=origin --push
      echo "[OK] Created and pushed ${OWNER}/${repo_name}"
    fi
  )
done

echo "[DONE] Project separation flow completed."
