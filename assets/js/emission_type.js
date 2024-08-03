let Highcharts;

let url = "https://raw.githubusercontent.com/preliminaries/abstracts/develop/data/emission_type.json";


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
        let data = [];
        for (let i = 0; i < source.data.length; i += 1) {

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
            series: [
                {
                    type: 'treegraph',
                    data,
                    tooltip: {
                        pointFormat: '{point.name}'
                    },
                    dataLabels: {
                        pointFormat: '{point.name}',
                        style: {
                            whiteSpace: 'nowrap',
                            color: '#000000',
                            textOutline: '3px contrast'
                        },
                        crop: false
                    },
                    marker: {
                        radius: 6
                    },
                    levels: [
                        {
                            level: 1,
                            dataLabels: {
                                align: 'left',
                                x: 20
                            }
                        },
                        {
                            level: 2,
                            colorByPoint: true,
                            dataLabels: {
                                verticalAlign: 'bottom',
                                y: -20
                            }
                        },
                        {
                            level: 3,
                            colorVariation: {
                                key: 'brightness',
                                to: -0.5
                            },
                            dataLabels: {
                                verticalAlign: 'top',
                                rotation: 0,
                                y: 20
                            }
                        }
                    ]
                }
            ]
        });

    });