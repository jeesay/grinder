// Fonction pour dessiner l'histogramme
function renderDistribution(jsonPath) {
    d3.json(jsonPath).then(rawData => {
        const values = rawData.data_micrographs.map(d => +d["_rlnAccumMotionTotal #5"]);
        
        // --- CALCULS STATS ---
        const mean = d3.mean(values);
        const median = d3.median(values);
        d3.select("#mean-val").text(mean.toFixed(1));
        d3.select("#median-val").text(median.toFixed(1));

        // --- CONFIGURATION ---
        const margin = {top: 40, right: 40, bottom: 50, left: 60},
              width = 700 - margin.left - margin.right,
              height = 400 - margin.top - margin.bottom;

        const svg = d3.select("#motion-dist-chart").append("svg")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .append("g").attr("transform", `translate(${margin.left},${margin.top})`);

        // --- GÉNÉRATION DES BINS (Tranches) ---
        const x = d3.scaleLinear().domain([0, 100]).range([0, width]); // On tronque à 100 
        
        const histogram = d3.bin()
            .domain(x.domain())
            .thresholds(x.ticks(40)); // Nombre de barres

        const bins = histogram(values);

        const y = d3.scaleLinear()
            .domain([0, d3.max(bins, d => d.length)])
            .nice()
            .range([height, 0]);

        // --- AXES ---
        svg.append("g").attr("transform", `translate(0,${height})`).call(d3.axisBottom(x));
        svg.append("g").call(d3.axisLeft(y));

        // --- BARRES ---
        svg.selectAll("rect")
            .data(bins)
            .enter().append("rect")
            .attr("x", d => x(d.x0) + 1)
            .attr("y", d => y(d.length))
            .attr("width", d => Math.max(0, x(d.x1) - x(d.x0) - 1))
            .attr("height", d => height - y(d.length))
            .attr("fill", "#56b494"); // Couleur verte de ton image

        // --- LIGNE DE SEUIL (Interative) ---
        const thresholdLine = svg.append("line")
            .attr("x1", x(50)).attr("x2", x(50))
            .attr("y1", 0).attr("y2", height)
            .attr("stroke", "#e15759").attr("stroke-dasharray", "4")
            .attr("stroke-width", 2);

        const thresholdText = svg.append("text")
            .attr("x", x(50) + 5).attr("y", 10)
            .attr("fill", "#e15759").text("50 Å");

        // --- MISE À JOUR DU SEUIL ---
        d3.select("#threshold-slider").on("input", function() {
            const val = +this.value;
            d3.select("#threshold-display").text(val);
            thresholdLine.attr("x1", x(val)).attr("x2", x(val));
            thresholdText.attr("x", x(val) + 5).text(val + " Å");
            
            // On peut ici calculer le % de rejeté :
            const rejected = values.filter(v => v > val).length;
            const percent = (rejected / values.length * 100).toFixed(1);
            console.log(`Rejetés: ${percent}%`);
        });
    });
}

// Logique de navigation simplifiée
document.addEventListener("DOMContentLoaded", () => {
    // Simuler le clic sur l'onglet DataViz
    // Dans votre vrai moteur, cela viendrait de la lecture du fichier STAR
    const navBtn = document.createElement("button");
    navBtn.innerText = "DataViz";
    navBtn.onclick = () => {
        document.getElementById("dataviz-section").style.display = "block";
        drawHistogram("star_file.json"); 
    };
    document.getElementById("sidebar-tabs").appendChild(navBtn);
});