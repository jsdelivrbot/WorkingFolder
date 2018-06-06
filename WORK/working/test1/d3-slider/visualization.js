
var margin = {top: 0, left:0, right:0, bottom:0},
    height = 400 -margin.top - margin.bottom,
    width = 800 - margin.left -margin.right;

var svg = d3.select("#map")
    .append("svg")
    .attr("height", height + marging.top + margin.bottom)
    .attr("width", width + margin.left + margin.right)
    .append("g")
    .attr("transform", "translate("+margin.left + "," + margin.top +")");

d3.queue()
    .defer(d3.json, "data/geomap.json")
    .await(ready)

var projection = d3.geoMercator()
    .translate([width/ 2, height/ 2])
    .scale[100]


var path = d3.geoPath()
    .projection(projection)

function ready ( error, data) {
    console.log(data)


var geomap = topojson.feature(data, data.objects.geomap.geometries).features
console.log(geomap)

svgelement.selectAll(".geomap")
    .data(geomap)
    .attr("class", "geo")
    .attr("d", path)
};
