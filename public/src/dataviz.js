import { h } from "./dom.js";

export function drawHistogram(container, dt, config) {
    const colName = dt.columnNames()[0]; // On prend la colonne de données
    const values = dt.array(colName);
    
    const margin = {top: 10, right: 10, bottom: 30, left: 40};
    const width = container.clientWidth - margin.left - margin.right;
    const height = 200 - margin.top - margin.bottom;

    const svg = d3.select(container).append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
      .append("g")
        .attr("transform", `translate(${margin.left},${margin.top})`);

    const x = d3.scaleLinear().domain(d3.extent(values)).nice().range([0, width]);
    const bins = d3.bin().domain(x.domain()).thresholds(30)(values);
    const y = d3.scaleLinear().domain([0, d3.max(bins, d => d.length)]).range([height, 0]);

    svg.append("g").attr("transform", `translate(0,${height})`).call(d3.axisBottom(x).ticks(5));
    svg.append("g").call(d3.axisLeft(y).ticks(5));

    svg.selectAll("rect").data(bins).enter().append("rect")
        .attr("x", d => x(d.x0) + 1)
        .attr("y", d => y(d.length))
        .attr("width", d => Math.max(0, x(d.x1) - x(d.x0) - 1))
        .attr("height", d => height - y(d.length))
        .attr("fill", "#56b494");
}

export function drawScatterPlot(container, dt, config) {
    const cols = dt.columnNames();
    const xName = cols[0]; // Souvent l'index
    const yName = cols[1]; // La valeur (ex: motion)
    
    const margin = {top: 10, right: 10, bottom: 30, left: 40};
    const width = container.clientWidth - margin.left - margin.right;
    const height = 200 - margin.top - margin.bottom;

    const svg = d3.select(container).append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
      .append("g")
        .attr("transform", `translate(${margin.left},${margin.top})`);

    const x = d3.scaleLinear().domain(d3.extent(dt.array(xName))).range([0, width]);
    const y = d3.scaleLinear().domain(d3.extent(dt.array(yName))).nice().range([height, 0]);

    svg.append("g").attr("transform", `translate(0,${height})`).call(d3.axisBottom(x).ticks(5));
    svg.append("g").call(d3.axisLeft(y).ticks(5));

    svg.append('path')
        .datum(dt.objects())
        .attr("fill", "none")
        .attr("stroke", "#4682b4")
        .attr("stroke-width", 1.5)
        .attr("d", d3.line()
            .x(d => x(d[xName]))
            .y(d => y(d[yName]))
        );
}

export function g_graphics(desc) {
    // grid: ncols,nrows????
    console.info("GRAPHIC", desc);
    const canvas = h(
        `canvas#${desc.id}.${desc.widget}`,
        { 
            // attrs: {width:200,height:100},
            on: {change: (ev) => console.log('change')}
        }
    )
    return canvas;
}