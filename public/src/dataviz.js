import { h } from "./dom.js";
import * as d3 from "https://cdn.skypack.dev/d3@7";



/////////////// HISTOGRAM ///////////////

export function drawHistogram(container, data, config) {
    const colName = Object.keys(data)[0];
    const allValues = data[colName].map(Number).filter(v => isFinite(v));

    // Coupure des outliers au 99e percentile
    const sorted = [...allValues].sort((a, b) => a - b);
    const p99 = sorted[Math.floor(sorted.length * 0.99)];
    const values = allValues.filter(v => v <= p99);

    d3.select(container).selectAll("*").remove();

    const margin = { top: 20, right: 20, bottom: 40, left: 50 };
    const width = container.clientWidth - margin.left - margin.right;
    const height = 250 - margin.top - margin.bottom;

    const svg = d3.select(container)
        .append("svg")
        .attr("viewBox", `0 0 ${width + margin.left + margin.right} ${height + margin.top + margin.bottom}`)
        .append("g")
        .attr("transform", `translate(${margin.left},${margin.top})`);

    const x = d3.scaleLinear()
        .domain([0, p99]).nice()
        .range([0, width]);

    const bins = d3.bin()
        .domain(x.domain())
        .thresholds(x.ticks(50))
        (values);

    const y = d3.scaleLinear()
        .domain([0, d3.max(bins, d => d.length)]).nice()
        .range([height, 0]);

    // Axes
    svg.append("g")
        .attr("transform", `translate(0,${height})`)
        .call(d3.axisBottom(x).ticks(6).tickFormat(d3.format(",.0f")));
    svg.append("g")
        .call(d3.axisLeft(y).ticks(6));

    // X axis label
    svg.append("text")
        .attr("x", width / 2)
        .attr("y", height + margin.bottom - 4)
        .attr("text-anchor", "middle")
        .style("font-size", "12px")
        .text(colName);

    // Bars
    svg.selectAll("rect")
        .data(bins)
        .join("rect")
        .attr("x", d => x(d.x0) + 1)
        .attr("width", d => Math.max(0, x(d.x1) - x(d.x0) - 1))
        .attr("y", d => y(d.length))
        .attr("height", d => height - y(d.length))
        .attr("fill", "#56b494");
}


/////////////// SCATTER PLOT  ///////////////


export function drawScatterPlot(container, data, config) {
    const keys = Object.keys(data);
    const xName = keys.includes('rlnIndex') ? 'rlnIndex' : keys[0];
    const yName = keys.length > 1 ? keys[1] : keys[0];

    const xValues = data[xName].map(Number);
    const yValues = data[yName].map(Number);
    const points = xValues.map((d, i) => ({x: d, y: yValues[i]}));

    d3.select(container).selectAll("*").remove();

    const margin = {top: 20, right: 20, bottom: 40, left: 50};
    const width = container.clientWidth - margin.left - margin.right;
    const height = 250 - margin.top - margin.bottom;

    const svg = d3.select(container)
        .append("svg")
        .attr("viewBox", `0 0 ${width + margin.left + margin.right} ${height + margin.top + margin.bottom}`)
        .append("g")
        .attr("transform", `translate(${margin.left},${margin.top})`);

    const x = d3.scaleLinear().domain(d3.extent(xValues)).range([0, width]);
    const y = d3.scaleLinear().domain(d3.extent(yValues)).nice().range([height, 0]);

    svg.append("g").attr("transform", `translate(0,${height})`).call(d3.axisBottom(x));
    svg.append("g").call(d3.axisLeft(y));

    svg.append("path")
        .datum(points)
        .attr("fill", "none")
        .attr("stroke", "#4682b4")
        .attr("stroke-width", 1.5)
        .attr("d", d3.line()
            .x(d => x(d.x))
            .y(d => y(d.y))
        );
}

/////////////// MICROGRAPHS TABLE  ///////////////

export function renderTable(container, data, config) {
    const colNames = Object.keys(data);
    console.log("colNames :", colNames)

    const totalRows = data[colNames[0]].length;
    console.log("data test (nbr mics) : ", data[colNames[0]].length)

    const table = document.createElement("table");
    table.className = "grinder-star-table"; // Optional : CSS style

    const thead = document.createElement("thead");
    const tbody = document.createElement("tbody");

    // 3. Headers (Th)
    const headerTr = document.createElement("tr");
    colNames.forEach(col => {
        const th = document.createElement("th");
        headerTr.appendChild(th);
    });
    thead.appendChild(headerTr);
    table.appendChild(thead);

    // 4. Lines (Td) with DocumentFragment
    const fragment = document.createDocumentFragment();

    for (let i = 0; i < totalRows; i++) {
        const tr = document.createElement("tr");
        
        // click event on target
        tr.addEventListener("click", () => {
            const mrcPath = data["rlnMicrographName"] ? data["rlnMicrographName"][i] : null;
            console.log(`Line ${i} selected. Corresponding micrograph :`, mrcPath);
            
            // TODO : display .webP
            if (mrcPath) {
                // window.dispatchEvent or instant call to display function WebP
            }
        });

        // filling cells for line i
        colNames.forEach(col => {
            const td = document.createElement("td");
            const value = data[col][i];
            td.textContent = (value !== undefined && value !== null) ? value : "-";
            tr.appendChild(td);
        });

        fragment.appendChild(tr);
    }

    // 5. DOM injection
    tbody.appendChild(fragment);
    table.appendChild(tbody);
    container.appendChild(table);

    console.log(`Table rendered successfully : ${totalRows} lines and ${colNames.length} columns.`);
}


/////////////// CORE  ///////////////

export function g_graphics(desc) {
    // grid: ncols,nrows????
    console.info("GRAPHIC", desc);
    const canvas = h(
        // `canvas#${desc.id}.${desc.widget}`,
        `div#${desc.id}.${desc.widget}.canvas`,
        { 
            // attrs: {width:200,height:100},
            on: {change: (ev) => console.log('change')}
        }
    )
    return canvas;
}