<!DOCTYPE html>
<head>    
    <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
    
        <script>
            L_NO_TOUCH = false;
            L_DISABLE_3D = false;
        </script>
    
    <script src="https://cdn.jsdelivr.net/npm/leaflet@1.5.1/dist/leaflet.js"></script>
    <script src="https://code.jquery.com/jquery-1.12.4.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/leaflet@1.5.1/dist/leaflet.css"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css"/>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css"/>
    <link rel="stylesheet" href="https://rawcdn.githack.com/python-visualization/folium/master/folium/templates/leaflet.awesome.rotate.css"/>
    <style>html, body {width: 100%;height: 100%;margin: 0;padding: 0;}</style>
    <style>#map {position:absolute;top:0;bottom:0;right:0;left:0;}</style>
    
            <meta name="viewport" content="width=device-width,
                initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
            <style>
                #map_93f95519dead4b89a1aefab2e7e7b2b0 {
                    position: relative;
                    width: 100.0%;
                    height: 100.0%;
                    left: 0.0%;
                    top: 0.0%;
                }
            </style>
        
</head>
<body>    
    
            <div class="folium-map" id="map_93f95519dead4b89a1aefab2e7e7b2b0" ></div>
        
</body>
<script>    
    
            var map_93f95519dead4b89a1aefab2e7e7b2b0 = L.map(
                "map_93f95519dead4b89a1aefab2e7e7b2b0",
                {
                    center: [-16.75, 36.5],
                    crs: L.CRS.EPSG3857,
                    maxBounds: [[-25.0, 30.0], [-8.5, 43.0]],
                    zoom: 10,
                    zoomControl: true,
                    preferCanvas: false,
                }
            );

            

        
    
            var tile_layer_ffd5b8ada18546049f134eda4a5f38d3 = L.tileLayer(
                "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
                {"attribution": "Data by \u0026copy; \u003ca href=\"http://openstreetmap.org\"\u003eOpenStreetMap\u003c/a\u003e, under \u003ca href=\"http://www.openstreetmap.org/copyright\"\u003eODbL\u003c/a\u003e.", "detectRetina": false, "maxNativeZoom": 18, "maxZoom": 18, "minZoom": 5, "noWrap": false, "opacity": 1, "subdomains": "abc", "tms": false}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
            map_93f95519dead4b89a1aefab2e7e7b2b0.fitBounds(
                [[-25.0, 30.0], [-8.5, 43.0]],
                {}
            );
        
    
            var marker_07cfe643efbd411888a6c062df0871d6 = L.marker(
                [-16.8536831, 36.966587],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_b69616da14cb49a9b26e74aeebc421c0 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_07cfe643efbd411888a6c062df0871d6.setIcon(custom_icon_b69616da14cb49a9b26e74aeebc421c0);
        
    
            var marker_bc6b1df2c8864637bcf01c813141b8bf = L.marker(
                [-13.2721452, 35.2640604],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_ec62b95092504c80a64898334ecacdcc = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_bc6b1df2c8864637bcf01c813141b8bf.setIcon(custom_icon_ec62b95092504c80a64898334ecacdcc);
        
    
            var marker_4eff4ae698154023a9f7956611fbd66a = L.marker(
                [-21.5362894, 35.4731954],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_416ba3bb3f65440cb56d3dc122fef448 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_4eff4ae698154023a9f7956611fbd66a.setIcon(custom_icon_416ba3bb3f65440cb56d3dc122fef448);
        
    
            var marker_6e392459791f4ac3ae62ab81048c04f2 = L.marker(
                [-21.1625508, 34.5610696],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_c635d8961c2e49f081afb35d497386d2 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_6e392459791f4ac3ae62ab81048c04f2.setIcon(custom_icon_c635d8961c2e49f081afb35d497386d2);
        
    
            var marker_216fd15af0d94035972330fd27c38c11 = L.marker(
                [-25.2659855, 33.2385979],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_16e9df28f5604b0c82cf6b13cf5f28ba = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_216fd15af0d94035972330fd27c38c11.setIcon(custom_icon_16e9df28f5604b0c82cf6b13cf5f28ba);
        
    
            var marker_94483e07cac843e5b0878a12bb4c6adf = L.marker(
                [-14.8159887, 36.5316201],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_50415c3ab4be48ac8f55895c2e117eaa = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_94483e07cac843e5b0878a12bb4c6adf.setIcon(custom_icon_50415c3ab4be48ac8f55895c2e117eaa);
        
    
            var marker_c5f0ad4e601444c3bd10cd24a32f171c = L.marker(
                [-25.9971447, 32.9293518],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_01a2d683f39e48a0945700aaed405040 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_c5f0ad4e601444c3bd10cd24a32f171c.setIcon(custom_icon_01a2d683f39e48a0945700aaed405040);
        
    
            var marker_7689e35113c94d90b313d93879f6030b = L.marker(
                [-11.6729002, 39.5630989],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_6e46419bd8504cab96171ce5673ad128 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_7689e35113c94d90b313d93879f6030b.setIcon(custom_icon_6e46419bd8504cab96171ce5673ad128);
        
    
            var marker_e5a97629a9d64d6f9a45484bbadf7f10 = L.marker(
                [-26.8285522, 32.8377075],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_28e52ef6a3724370b9b5528ea556acba = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_e5a97629a9d64d6f9a45484bbadf7f10.setIcon(custom_icon_28e52ef6a3724370b9b5528ea556acba);
        
    
            var marker_1edb4ea48d644af8bdabb30338610c68 = L.marker(
                [-15.6027002, 32.773201],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_ea33bdb34562452dbe5b193d6f166ee0 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_1edb4ea48d644af8bdabb30338610c68.setIcon(custom_icon_ea33bdb34562452dbe5b193d6f166ee0);
        
    
            var marker_9222084fc4b34c11bfff3270b0ab5a13 = L.marker(
                [-14.7054025, 34.353037],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_a0f3672d9c4340bf94b186ec56280f5c = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_9222084fc4b34c11bfff3270b0ab5a13.setIcon(custom_icon_a0f3672d9c4340bf94b186ec56280f5c);
        
    
            var marker_5e7f155c1bf14b9fb3e16e69e60d6b02 = L.marker(
                [-25.0377998, 33.6273994],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_9d8f6903560c43ca91471472e23a999d = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_5e7f155c1bf14b9fb3e16e69e60d6b02.setIcon(custom_icon_9d8f6903560c43ca91471472e23a999d);
        
    
            var marker_7d1998a567c442a496250eb6cae44581 = L.marker(
                [-21.7080002, 35.4528008],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_0adfee6e5db0471093e67aeb7259bce6 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_7d1998a567c442a496250eb6cae44581.setIcon(custom_icon_0adfee6e5db0471093e67aeb7259bce6);
        
    
            var marker_7b21ee50f6f54327b68dcf06f81b6d72 = L.marker(
                [-13.1218996, 39.0527992],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_d431dd79512d4017a3ac8c4b9b0f6237 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_7b21ee50f6f54327b68dcf06f81b6d72.setIcon(custom_icon_d431dd79512d4017a3ac8c4b9b0f6237);
        
    
            var marker_b202f1a90f6e4aebbf4785e04b2ec6c1 = L.marker(
                [-21.6149998, 35.3380013],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_f67f4c6ae45f4da3b3bec3a1aeedb12b = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_b202f1a90f6e4aebbf4785e04b2ec6c1.setIcon(custom_icon_f67f4c6ae45f4da3b3bec3a1aeedb12b);
        
    
            var marker_6655806a2cf4430c9677565dd243af1f = L.marker(
                [-19.7997428, 34.9176636],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_78a6a07b270147c99f1fa1859ab15f1e = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_6655806a2cf4430c9677565dd243af1f.setIcon(custom_icon_78a6a07b270147c99f1fa1859ab15f1e);
        
    
            var marker_5c2de33851f44035ae95e37a514e6e21 = L.marker(
                [-26.802856, 32.8835637],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_5406997b33924b68ae755f703b105a9b = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_5c2de33851f44035ae95e37a514e6e21.setIcon(custom_icon_5406997b33924b68ae755f703b105a9b);
        
    
            var marker_67b9ff0972e1490dbddbbaf3512dd552 = L.marker(
                [-25.0319515, 32.7483858],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_dc43e0173a3b42e69d993854bec5f664 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_67b9ff0972e1490dbddbbaf3512dd552.setIcon(custom_icon_dc43e0173a3b42e69d993854bec5f664);
        
    
            var marker_5bf44b201ee7401fb1af32a80d2f7d23 = L.marker(
                [-22.8208754, 32.0042977],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_9b77a425a1fd42dcb4df2368e83a8e8d = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_5bf44b201ee7401fb1af32a80d2f7d23.setIcon(custom_icon_9b77a425a1fd42dcb4df2368e83a8e8d);
        
    
            var marker_38018cf5398d46ec89f7e476c9aa73a4 = L.marker(
                [-21.5879383, 32.9292169],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_cc61a40d62da44dc8ab37d91c095a091 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_38018cf5398d46ec89f7e476c9aa73a4.setIcon(custom_icon_cc61a40d62da44dc8ab37d91c095a091);
        
    
            var marker_3715e95b889348bebcae266613e5f0df = L.marker(
                [-25.2376204, 32.1598927],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_200603bdbec4476380127b68237a42ba = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_3715e95b889348bebcae266613e5f0df.setIcon(custom_icon_200603bdbec4476380127b68237a42ba);
        
    
            var marker_919b5015e0ae4a8eba4619764ae29cd4 = L.marker(
                [-25.1995933, 33.5011298],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_dec21d4b2fad434ba99f89977243c183 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_919b5015e0ae4a8eba4619764ae29cd4.setIcon(custom_icon_dec21d4b2fad434ba99f89977243c183);
        
    
            var marker_2210e4d9a36e444dbb82a03000efa1b6 = L.marker(
                [-21.7532037, 35.0598754],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_91cbeb2d8c2c44ad8aa9cee1291f7056 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_2210e4d9a36e444dbb82a03000efa1b6.setIcon(custom_icon_91cbeb2d8c2c44ad8aa9cee1291f7056);
        
    
            var marker_217f6bfd4415447a8bcc818b7d249606 = L.marker(
                [-21.5264614, 35.4807876],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_265fa5330d8348e7937a7840c69ea4d9 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_217f6bfd4415447a8bcc818b7d249606.setIcon(custom_icon_265fa5330d8348e7937a7840c69ea4d9);
        
    
            var marker_bbba67ae348b4a699176652141195d0a = L.marker(
                [-12.2005615, 40.5689777],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_f4c837ba3e0f41debecaca9ce5eb6632 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_bbba67ae348b4a699176652141195d0a.setIcon(custom_icon_f4c837ba3e0f41debecaca9ce5eb6632);
        
    
            var marker_81385b470a6f489c87a396996464fd38 = L.marker(
                [-17.8631466, 36.8702758],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_144f8943521244b59f678ee8b0cc81a9 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_81385b470a6f489c87a396996464fd38.setIcon(custom_icon_144f8943521244b59f678ee8b0cc81a9);
        
    
            var marker_63b72b3e197b4501bdc99bf8a2b6aa29 = L.marker(
                [-23.9395556, 32.1538495],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_e94bcd4083e24967a153593e70813d12 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_63b72b3e197b4501bdc99bf8a2b6aa29.setIcon(custom_icon_e94bcd4083e24967a153593e70813d12);
        
    
            var marker_59969ae1aba241bdabec4a655d756fcf = L.marker(
                [-25.309864, 32.2587114],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_5091c32ac85245a6bb58726a01d049d9 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_59969ae1aba241bdabec4a655d756fcf.setIcon(custom_icon_5091c32ac85245a6bb58726a01d049d9);
        
    
            var marker_bec350e951ed4261b1b4aac094ca2b8d = L.marker(
                [-26.0461341, 32.2776677],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_aaf3490456134d7fb46930218a5b37ff = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_bec350e951ed4261b1b4aac094ca2b8d.setIcon(custom_icon_aaf3490456134d7fb46930218a5b37ff);
        
    
            var marker_d40643690a3f461e8f8c8e79e90ec677 = L.marker(
                [-12.3501793, 40.6019581],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_324ea2f6c05241e284a2571d7f582dee = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_d40643690a3f461e8f8c8e79e90ec677.setIcon(custom_icon_324ea2f6c05241e284a2571d7f582dee);
        
    
            var marker_db764af3bf944270ade36ca16ff23067 = L.marker(
                [-14.2110529, 40.6967906],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_42679f4db4fc4f27a604052e7edab1e3 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_db764af3bf944270ade36ca16ff23067.setIcon(custom_icon_42679f4db4fc4f27a604052e7edab1e3);
        
    
            var marker_74851a00caf3480a92619782eb07fd21 = L.marker(
                [-13.4070995, 39.8028527],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_31ea18f53f2440fda3c4be93f184d4ee = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_74851a00caf3480a92619782eb07fd21.setIcon(custom_icon_31ea18f53f2440fda3c4be93f184d4ee);
        
    
            var marker_03a2ba4ff4904055a48a6eda789294cf = L.marker(
                [-14.8790274, 40.0434146],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_71fd8f59a56e4602aa0dea08d2383b5f = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_03a2ba4ff4904055a48a6eda789294cf.setIcon(custom_icon_71fd8f59a56e4602aa0dea08d2383b5f);
        
    
            var marker_af434e772bc54d19af403242f3908180 = L.marker(
                [-15.5040186, 36.98669],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_a09a5a06771b4bbcb8d9aac1d75b082e = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_af434e772bc54d19af403242f3908180.setIcon(custom_icon_a09a5a06771b4bbcb8d9aac1d75b082e);
        
    
            var marker_84a8374fad894ea1875009cfa75fa14f = L.marker(
                [-15.7363258, 32.762586],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_0a37ece56b1245fa9112ac35e22a679a = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_84a8374fad894ea1875009cfa75fa14f.setIcon(custom_icon_0a37ece56b1245fa9112ac35e22a679a);
        
    
            var marker_62ca53d368784d1c9ce3192b89592aaa = L.marker(
                [-24.2247201, 35.4216259],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_79b24c04c1e74076b8317fe34469f33c = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_62ca53d368784d1c9ce3192b89592aaa.setIcon(custom_icon_79b24c04c1e74076b8317fe34469f33c);
        
    
            var marker_76cf1841d6d246e0a0ffba2ad45db684 = L.marker(
                [-11.3596821, 40.3538089],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_06bb89d583304c1d90fde5624b627ded = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_76cf1841d6d246e0a0ffba2ad45db684.setIcon(custom_icon_06bb89d583304c1d90fde5624b627ded);
        
    
            var marker_a950b54f10f6494bbff0e88af9b0bd6e = L.marker(
                [-10.7524932, 40.47087],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_2778c8c8b00e4fc091d72d3fbad38372 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_a950b54f10f6494bbff0e88af9b0bd6e.setIcon(custom_icon_2778c8c8b00e4fc091d72d3fbad38372);
        
    
            var marker_72ca75b36ad54270a8c9532db0477638 = L.marker(
                [-11.9008621, 37.1886348],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_d3efec5d81834ad7816fed2d3589a794 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_72ca75b36ad54270a8c9532db0477638.setIcon(custom_icon_d3efec5d81834ad7816fed2d3589a794);
        
    
            var marker_0bae706b723f4da9a40b17396b50d84a = L.marker(
                [-12.5498226, 36.2569637],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_7760d725b1f14f0dada94c8c1bddfa80 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_0bae706b723f4da9a40b17396b50d84a.setIcon(custom_icon_7760d725b1f14f0dada94c8c1bddfa80);
        
    
            var marker_82e39547b742459686cae12e271a0287 = L.marker(
                [-11.6412688, 37.1481759],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_2fd41f3bdbbd43f296f6dfcd73197c4e = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_82e39547b742459686cae12e271a0287.setIcon(custom_icon_2fd41f3bdbbd43f296f6dfcd73197c4e);
        
    
            var marker_c60312f5377b4b47b8498e21898e7c04 = L.marker(
                [-11.3401855, 38.3030171],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_cadb961bca2f4d0a9ce9ce5a594e453b = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_c60312f5377b4b47b8498e21898e7c04.setIcon(custom_icon_cadb961bca2f4d0a9ce9ce5a594e453b);
        
    
            var marker_1db9fdd4155649efa352509b4176f014 = L.marker(
                [-12.6018862, 36.5552365],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_c870f300649549b78b8bfa4d19f07ec1 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_1db9fdd4155649efa352509b4176f014.setIcon(custom_icon_c870f300649549b78b8bfa4d19f07ec1);
        
    
            var marker_ff50939a95dc42ffa81a0b0cf988f555 = L.marker(
                [-12.4660624, 37.6600486],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_61e7518ab90e4f46bcfe173259a5d180 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_ff50939a95dc42ffa81a0b0cf988f555.setIcon(custom_icon_61e7518ab90e4f46bcfe173259a5d180);
        
    
            var marker_ca61c4f6204042de85aa225f1156bfb2 = L.marker(
                [-12.2424529, 38.0001527],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_da013a9ada614aa5bc9f642b54be708d = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_ca61c4f6204042de85aa225f1156bfb2.setIcon(custom_icon_da013a9ada614aa5bc9f642b54be708d);
        
    
            var marker_432309dc6f104a2c98d15c6f80dbbe10 = L.marker(
                [-12.1403522, 38.3189937],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_f957dc25b6c5437f9b484f07967a15fc = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_432309dc6f104a2c98d15c6f80dbbe10.setIcon(custom_icon_f957dc25b6c5437f9b484f07967a15fc);
        
    
            var marker_c7ad7acdf1044b0794414fb95d9f6cc4 = L.marker(
                [-12.1515121, 38.2838889],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_6fcfbd801f0e434694d7a87264cee14d = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_c7ad7acdf1044b0794414fb95d9f6cc4.setIcon(custom_icon_6fcfbd801f0e434694d7a87264cee14d);
        
    
            var marker_e35e15cd9ead445799289f57e5c7f971 = L.marker(
                [-12.1696793, 37.54613],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_60c0a57ac14b4b4b920d98fb76840db6 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_e35e15cd9ead445799289f57e5c7f971.setIcon(custom_icon_60c0a57ac14b4b4b920d98fb76840db6);
        
    
            var marker_c53882e732ba4991963b81c5d84c2fc9 = L.marker(
                [-11.0729292, 39.6748264],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_1bbaab42eb36435899887da2bd26fc4d = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_c53882e732ba4991963b81c5d84c2fc9.setIcon(custom_icon_1bbaab42eb36435899887da2bd26fc4d);
        
    
            var marker_4dd921ce3808435f96fb4445e77b3004 = L.marker(
                [-17.8636198, 36.8703153],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_6e7c01f96d73456cadf8361dd7070f3d = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_4dd921ce3808435f96fb4445e77b3004.setIcon(custom_icon_6e7c01f96d73456cadf8361dd7070f3d);
        
    
            var marker_55933b7466644cf5a5a9c7db8d8fd5c1 = L.marker(
                [-16.1134508, 33.6397552],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_99bd1c1b1bad42898c5220aa248bfd38 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_55933b7466644cf5a5a9c7db8d8fd5c1.setIcon(custom_icon_99bd1c1b1bad42898c5220aa248bfd38);
        
    
            var marker_d2bc0d96667e44acad02091a26337483 = L.marker(
                [-16.113449, 33.6396726],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_0bd6bd81c7954b66bdb239e797d4e3de = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_d2bc0d96667e44acad02091a26337483.setIcon(custom_icon_0bd6bd81c7954b66bdb239e797d4e3de);
        
    
            var marker_9dc56eb3a2924663beeab1448c9bd740 = L.marker(
                [-16.1134473, 33.6395895],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_c9b906507e69498ab3d3b9962d98279e = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_9dc56eb3a2924663beeab1448c9bd740.setIcon(custom_icon_c9b906507e69498ab3d3b9962d98279e);
        
    
            var marker_3e8cd624fee04ab780eedb03db94106c = L.marker(
                [-16.1134454, 33.639501],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_571a85120e404ad799413717a6df434b = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_3e8cd624fee04ab780eedb03db94106c.setIcon(custom_icon_571a85120e404ad799413717a6df434b);
        
    
            var marker_ef4e4943621048f59e33d220a4d71b85 = L.marker(
                [-16.1134424, 33.6393642],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_9b9ef25179f74254892473b9a53f6941 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_ef4e4943621048f59e33d220a4d71b85.setIcon(custom_icon_9b9ef25179f74254892473b9a53f6941);
        
    
            var marker_3433d937ccea4f0380d9fdcd9a99c01e = L.marker(
                [-16.1254926, 33.6398068],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_c8f6f381209a42828e524d545ac485fa = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_3433d937ccea4f0380d9fdcd9a99c01e.setIcon(custom_icon_c8f6f381209a42828e524d545ac485fa);
        
    
            var marker_cf64cd43cba84f88816cd87f7082bc3a = L.marker(
                [-15.1999937, 35.8695997],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_fc696f9384e64c128bf7dd3e411f4033 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_cf64cd43cba84f88816cd87f7082bc3a.setIcon(custom_icon_fc696f9384e64c128bf7dd3e411f4033);
        
    
            var marker_1ab7024cb0ac41ea96b2a710ce7422f8 = L.marker(
                [-12.7015132, 34.8043578],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_d835dc5f79434467bcee8eef4e61929a = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_1ab7024cb0ac41ea96b2a710ce7422f8.setIcon(custom_icon_d835dc5f79434467bcee8eef4e61929a);
        
    
            var marker_b1e4d6e99e144e7e815ebfdb686bf078 = L.marker(
                [-26.3936269, 32.6508692],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_053784b76cc444c0b929a11e8255cb5e = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_b1e4d6e99e144e7e815ebfdb686bf078.setIcon(custom_icon_053784b76cc444c0b929a11e8255cb5e);
        
    
            var marker_623f17593f1242fdbd24588d6378f593 = L.marker(
                [-19.8933436, 34.5856456],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_46ebcf62436f4dd5bab4d7fcfa69d6e6 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_623f17593f1242fdbd24588d6378f593.setIcon(custom_icon_46ebcf62436f4dd5bab4d7fcfa69d6e6);
        
    
            var marker_5bace2940cd54f38abd207ee278a0c83 = L.marker(
                [-19.7952029, 34.896896],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_93269cbfef774ef2a3d64ce71905826b = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_5bace2940cd54f38abd207ee278a0c83.setIcon(custom_icon_93269cbfef774ef2a3d64ce71905826b);
        
    
            var marker_9efbb83f9316457aba6f1200d174c14c = L.marker(
                [-19.7999018, 34.9182957],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_5905407fc55b4939a263e5b3f84d9544 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_9efbb83f9316457aba6f1200d174c14c.setIcon(custom_icon_5905407fc55b4939a263e5b3f84d9544);
        
    
            var marker_79e81a5a03584738b65d43d5d489e3e7 = L.marker(
                [-19.7935243, 34.8993105],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_f938c5d88adf43d388dfa6f091338940 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_79e81a5a03584738b65d43d5d489e3e7.setIcon(custom_icon_f938c5d88adf43d388dfa6f091338940);
        
    
            var marker_c0cc65afb239435fac4cd0c4743111df = L.marker(
                [-19.7976317, 34.9061903],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_666c12f4c3ac4f97a2f59ed7125c3de4 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_c0cc65afb239435fac4cd0c4743111df.setIcon(custom_icon_666c12f4c3ac4f97a2f59ed7125c3de4);
        
    
            var marker_c2458b4d40674b2a8414241c283bac44 = L.marker(
                [-19.7995068, 34.9155539],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_2d3b4171d3dc4ec09754e60da0136a9e = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_c2458b4d40674b2a8414241c283bac44.setIcon(custom_icon_2d3b4171d3dc4ec09754e60da0136a9e);
        
    
            var marker_1a3d35f248dc44108e9b8aa2f94e3cb0 = L.marker(
                [-19.799879, 34.9214199],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_834eba07db8a465db505980fafeb55af = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_1a3d35f248dc44108e9b8aa2f94e3cb0.setIcon(custom_icon_834eba07db8a465db505980fafeb55af);
        
    
            var marker_8a575725864b43c5b77de9e947ad23f7 = L.marker(
                [-19.796438, 34.9045864],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_96c981fea7544df8b0fbfe2b97d4831c = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_8a575725864b43c5b77de9e947ad23f7.setIcon(custom_icon_96c981fea7544df8b0fbfe2b97d4831c);
        
    
            var marker_364ed820181e442fa320fb5784da4db3 = L.marker(
                [-17.8501549, 36.8689343],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_c410853aa9d9479299d49287aee529e0 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_364ed820181e442fa320fb5784da4db3.setIcon(custom_icon_c410853aa9d9479299d49287aee529e0);
        
    
            var marker_3fa5ffa790724055a2fd089c33a39871 = L.marker(
                [-17.8587714, 36.8698007],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_f5c81084ddf94253b58a530d8bc9dc23 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_3fa5ffa790724055a2fd089c33a39871.setIcon(custom_icon_f5c81084ddf94253b58a530d8bc9dc23);
        
    
            var marker_2a4e578fd8614feb927d295537dc94ed = L.marker(
                [-19.1489727, 33.4278915],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_373ba7c9175f4c04b0a5c662d5e06904 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_2a4e578fd8614feb927d295537dc94ed.setIcon(custom_icon_373ba7c9175f4c04b0a5c662d5e06904);
        
    
            var marker_452e77bb00344025a33f0aef38dbc5d6 = L.marker(
                [-19.1479985, 33.4282918],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_3186f351e2204c65a72ac5f93c22a322 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_452e77bb00344025a33f0aef38dbc5d6.setIcon(custom_icon_3186f351e2204c65a72ac5f93c22a322);
        
    
            var marker_746903599d054beb9631cc7f806384d4 = L.marker(
                [-19.1499533, 33.4281135],
                {"iconSize": [14, 14]}
            ).addTo(map_93f95519dead4b89a1aefab2e7e7b2b0);
        
    
        var custom_icon_4e9222a5eb044e77b62cbde46a203fc5 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_746903599d054beb9631cc7f806384d4.setIcon(custom_icon_4e9222a5eb044e77b62cbde46a203fc5);
        
</script>