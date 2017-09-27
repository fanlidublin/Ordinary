d3.selectAll("rect")
    .style("stroke","purple")
    .style("stroke-width", "2")

d3.selectAll("line")
    .style("stroke", "green")

// for id
d3.select("#special_par")
    .style("fill","red")

// for class
d3.select(".secret")
    .style("color","blue")

d3.selectAll("rect")
    .remove()

d3.select(".secret")
    .remove()

d3.select("svg")
    .append("rect")
    .attr("y","25")
    .attr("width","100")
    .attr("height","50")
    .style("fill","black")
    .style("opacity","0.5")

d3.select("body")
    .append("p",".line-numbers")
    .text("Brought to you by University College Dublin")

d3.select("body")
    .insert("p","#test")
    .text("Modified on Wednesday")
