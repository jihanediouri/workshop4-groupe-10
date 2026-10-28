# Script PowerShell pour lancer le scan ZAP Baseline via Docker
# Assurez-vous que l'application est lancée au préalable sur http://localhost:5000

Write-Host "Lancement du scan ZAP Baseline sur http://localhost:5000..."

docker run --rm -v ${PWD}:/zap/wrk/:rw -t ghcr.io/zaproxy/zaproxy:stable zap-baseline.py `
    -t http://host.docker.internal:5000 `
    -r zap_report.html

Write-Host "Scan terminé. Le rapport est disponible dans zap_report.html"
