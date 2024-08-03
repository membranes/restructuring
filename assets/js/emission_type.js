var Highcharts;

var url = "https://raw.githubusercontent.com/preliminaries/abstracts/develop/data/emission_type.json"


// Generate curves
jQuery.getJSON(url,
    function (source) {

        // Indices
        let columns = source.columns;
        let id = columns.indexOf('id'),
            pa = columns.indexOf('parent'),
            na = columns.indexOf('name'),
            de = columns.indexOf('description');

        // Data
        var data = [];
        for (var i = 0; i < source.data.length; i += 1) {

            // parent, child
            data.push([
                source.data[i][id],
                source.data[i][pa],
                source.data[i][na],
                source.data[i][de]
            ]);

        }


        Highcharts.chart('container', {
            chart: {
                inverted: false,
                height: 500,
                marginTop: 5
            },
            title: {
                text: 'Proposal: Emission Source Types',
                align: 'left'
            },
            subtitle: {
                text: 'Climate & Sustainability',
                align: 'left'
            },
            plotOptions: {
                treegraph: {
                    dataLabels: {
                        enabled: true
                    }
                }
            },
            caption: {
                verticalAlign: "bottom",
                y: -135,
                x: 85,
                text: '<p>A data model</p>'
            },
            series: []
        });

    });