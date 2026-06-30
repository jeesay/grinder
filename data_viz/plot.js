import {StarGate} from "./stargate.js";

// UTILS

function stripQuotes(str) {
    if (typeof str !== "string") return str;
    return str.replace(/^["']|["']$/g, "");
}

function parseValue(value) {
    const obj = {};
    if (!value) return obj;

    value = stripQuotes(value);

    value.split(";").forEach(p => {
        const [k, v] = p.split(":");
        if (k && v) obj[k.trim()] = v.trim();
    });

    return obj
}

// MAIN

function parseDataViz(block) {
    const rows = block.table("dataviz");
    if (!rows) return [];

    return rows.map(row => {
        const clean = {};

        for (let key in row) {
            const newKey = key.split(".").pop();
            clean[newKey] = stripQuotes(row[key]);
        }

        const tok = parseValue(clean.value);

        return {
            id: clean.id,
            lael: clean.label,
            widget: clean.widget,
            x: tok.x || "index",
            y: tok.y,
            source: tok.source,
            style: tok.style || "dots",
            color: tok.color || "#00f",

            // debug
            raw: clean
        };
    });
}

async function renderPlot(config) {
    const res = await fetch("data.json");
    const data = await res.json();

    const trace = {
        x: data.x,
        y: data.y,
        mode: config.style === "dots" ? "markers" : "lines",
        marker: {color: config.color}
    };

    Plotly.newPlot(config.id, [trace], {
        title: config.label
    });
}

const sg = new StarGate();
sg.parseSTAR(txt);

const block = sg.datablock("rln_mc");

const plots = parseDataViz(block);

plots.forEach(config => {
    if (config.widget === "plot2d") {
        renderPlot(config);
    }
});

