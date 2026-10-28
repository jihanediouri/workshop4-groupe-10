# Script pour lancer le scan ZAP Baseline via Docker
# Assurez-vous que l'application est lancée au préalable sur http://localhost:5000

echo "Lancement du scan ZAP Baseline sur http://localhost:5000..."

# On utilise le réseau hôte pour que le conteneur ZAP puisse accéder à l'app locale
# Ou on passe l'IP de la machine hôte. Sur Windows/Mac, host.docker.internal fonctionne souvent.

docker run --rm -v $(pwd):/zap/wrk/:rw -t ghcr.io/zaproxy/zaproxy:stable zap-baseline.py \
    -t http://host.docker.internal:5000 \
    -r zap_report.html

echo "Scan terminé. Le rapport est disponible dans zap_report.html"
