# Script PowerShell pour lancer le scan ZAP Actif (Full Scan) via Docker
# ATTENTION : À ne lancer que sur des instances de pré-prod/test !

Write-Host "Lancement du scan ZAP Full (Actif) sur http://localhost:5000..."

docker run --rm -v ${PWD}:/zap/wrk/:rw -t ghcr.io/zaproxy/zaproxy:stable zap-full-scan.py `
    -t http://host.docker.internal:5000 `
    -r zap_full_report.html

Write-Host "Scan actif terminé. Rapport : zap_full_report.html"
