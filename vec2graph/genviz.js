(function(){
'use strict';

document.addEventListener("DOMContentLoaded", function(e) {
  var width = 100, height = 100;
  var maincolor = "#F4B400";
  var svg = d3.select("body").append("svg");
  var force = d3.layout.force().gravity(.05).distance(100).charge(-100);
  var datanodes = [], datalinks = [], i = 1;
  var delta = 0;
  var radius = 10;

  function getMeta(metaName) {
  var metas = document.getElementsByTagName('meta');

  for (let i = 0; i < metas.length; i++) {
    if (metas[i].getAttribute('name') === metaName) {
      return metas[i].getAttribute('content');
    };
    }
    return '';
  };

  var splithyphen = getMeta("split-hyphen");
  var data = JSON.parse(getMeta("data"));
  var topn = getMeta("number-of-neighbours");
  var linkstrokewidth = getMeta("link-stroke-width");
  var pages = JSON.parse(getMeta("pages"));
  var threshold = getMeta("threshold");


  function buildGraph(inlinks, innodes) {
    d3.selectAll(".link").remove();
    d3.selectAll(".node").remove();
    d3.selectAll("circle").remove();
    var links = inlinks;
    force.nodes(innodes).links(inlinks).linkDistance(function(d) {
      var dv = d.value * 100;
      var df = Math.log(dv);
      var koef = isFinite(df) ? df : 1;
      return dv * koef + radius;
    }).start();
    var linksel = svg.selectAll(".link").data(inlinks);
    var link = linksel.enter().append("line").attr("stroke", "#aaa").style("stroke-width", linkstrokewidth || 1);
    var nodesel = svg.selectAll(".node").data(innodes);
    var node = nodesel.enter().append("g").call(force.drag);
    node.append("circle").attr("fill", function(d) {
      return d.color;
    }).style("stroke", "black").style("stroke-width", function(d) {
      return d.page ? 3 : 0;
    }).attr("r", function(d) {
      return d.color == maincolor ? radius * 1.5 : radius;
    }).on("click", function(d) {
      if (d.page) {
        window.open(d.name + ".html");
      }
    });
    node.append("text").text(function(d) {
      return splithyphen === 'true' ? d.name.split("_")[0] : d.name;
    }).on("click", function(d) {
      if (d.page) {
        window.open(d.name + ".html");
      }
    }).attr("stroke", "#333").attr("dx", 12).attr("dy", ".35em").style("cursor", "default");
    nodesel.exit().remove();
    force.on("tick", function() {
      link.attr("x1", function(d) {
        return d.source.x;
      }).attr("y1", function(d) {
        return d.source.y;
      }).attr("x2", function(d) {
        return d.target.x;
      }).attr("y2", function(d) {
        return d.target.y;
      });
      node.attr("transform", function(d) {
        return "translate(" + d.x + "," + d.y + ")";
      });
    });
  }
  width = window.innerWidth, height = window.innerHeight;
  svg.attr("width", width).attr("height", height);
  force.size([width, height]);
  var order = {};
  order[data[0]["source"]] = 0;
  datanodes.push({"name":data[0]["source"], color:maincolor});
  for (var k, k = 1; k < data.length; k++) {
    var dif = 1 - data[k]["value"];
    if (delta && delta > dif || !delta) {
      delta = dif;
    }
    var key = data[k]["target"];
    var src = 0;
    var tg = k;
    if (k > topn) {
      src = order[data[k]["source"]];
      tg = order[data[k]["target"]];
    } else {
      datanodes.push({"name":data[k]["target"], color:"#DB4437", page:pages.indexOf(data[k]["target"]) > -1});
      order[key] = k;
    }
    if (data[k]["value"] > threshold) {
      datalinks.push({"source":src, "target":tg, "value":dif, "key":key});
    }
  }
  buildGraph(datalinks, datanodes);
});

}).call(this)