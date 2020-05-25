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
                #map_908d913a32b24391b93547490dfdad73 {
                    position: relative;
                    width: 100.0%;
                    height: 100.0%;
                    left: 0.0%;
                    top: 0.0%;
                }
            </style>
        
</head>
<body>    
    
            <div class="folium-map" id="map_908d913a32b24391b93547490dfdad73" ></div>
        
</body>
<script>    
    
            var map_908d913a32b24391b93547490dfdad73 = L.map(
                "map_908d913a32b24391b93547490dfdad73",
                {
                    center: [-16.75, 36.5],
                    crs: L.CRS.EPSG3857,
                    maxBounds: [[-25.0, 30.0], [-8.5, 43.0]],
                    zoom: 10,
                    zoomControl: true,
                    preferCanvas: false,
                }
            );

            

        
    
            var tile_layer_3c459073294a40a5bf0f72484b7026bb = L.tileLayer(
                "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
                {"attribution": "Data by \u0026copy; \u003ca href=\"http://openstreetmap.org\"\u003eOpenStreetMap\u003c/a\u003e, under \u003ca href=\"http://www.openstreetmap.org/copyright\"\u003eODbL\u003c/a\u003e.", "detectRetina": false, "maxNativeZoom": 18, "maxZoom": 18, "minZoom": 5, "noWrap": false, "opacity": 1, "subdomains": "abc", "tms": false}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
            map_908d913a32b24391b93547490dfdad73.fitBounds(
                [[-25.0, 30.0], [-8.5, 43.0]],
                {}
            );
        
    
            var marker_7cc6462c321944d3bf2a1700a2600aeb = L.marker(
                [-16.8536831, 36.966587],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_4539ae0001bb4520955632b94c438fdf = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_7cc6462c321944d3bf2a1700a2600aeb.setIcon(custom_icon_4539ae0001bb4520955632b94c438fdf);
        
    
            var marker_5adb166dc0e44cbe91d1906081443b57 = L.marker(
                [-13.2721452, 35.2640604],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_fff675b6aa1c4537b457baa6f710b3f5 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_5adb166dc0e44cbe91d1906081443b57.setIcon(custom_icon_fff675b6aa1c4537b457baa6f710b3f5);
        
    
            var marker_71762b5787474f18b8bf3eebeb4a57b1 = L.marker(
                [-21.5362894, 35.4731954],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_d335ea980489483c9818fc7ef0f0fef2 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_71762b5787474f18b8bf3eebeb4a57b1.setIcon(custom_icon_d335ea980489483c9818fc7ef0f0fef2);
        
    
            var marker_f8c0907b05164eb490d8f6232d36558e = L.marker(
                [-21.1625508, 34.5610696],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_05b26ae3e48f4495a8005bd1aca1a2bf = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_f8c0907b05164eb490d8f6232d36558e.setIcon(custom_icon_05b26ae3e48f4495a8005bd1aca1a2bf);
        
    
            var marker_3b5554dc165545b9978921916716eda7 = L.marker(
                [-25.2659855, 33.2385979],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_2895b03b26b047769556efad0c29fb1a = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_3b5554dc165545b9978921916716eda7.setIcon(custom_icon_2895b03b26b047769556efad0c29fb1a);
        
    
            var marker_13f54e88d1db45d986f10c750897b182 = L.marker(
                [-14.8159887, 36.5316201],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_983136740c4a4efd89370312475a7a41 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_13f54e88d1db45d986f10c750897b182.setIcon(custom_icon_983136740c4a4efd89370312475a7a41);
        
    
            var marker_572615d17063415ab92158efecde8215 = L.marker(
                [-25.9971447, 32.9293518],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_499d735246924e21aa2afac7faf23474 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_572615d17063415ab92158efecde8215.setIcon(custom_icon_499d735246924e21aa2afac7faf23474);
        
    
            var marker_583cb35788a84943b07ad8a4e8defe18 = L.marker(
                [-11.6729002, 39.5630989],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_9e9cf8aebd6f44559171eb0a6a1cd4f0 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_583cb35788a84943b07ad8a4e8defe18.setIcon(custom_icon_9e9cf8aebd6f44559171eb0a6a1cd4f0);
        
    
            var marker_da71da5900a14dfd8d717dfa16f1cbac = L.marker(
                [-26.8285522, 32.8377075],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_3d96137ba2404bbf8f3c2d1a50b5d068 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_da71da5900a14dfd8d717dfa16f1cbac.setIcon(custom_icon_3d96137ba2404bbf8f3c2d1a50b5d068);
        
    
            var marker_d4eadf1feeb14151b6a01b55d5e19bfd = L.marker(
                [-15.6027002, 32.773201],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_0f080ebf56e045b88c695028dc6468f8 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_d4eadf1feeb14151b6a01b55d5e19bfd.setIcon(custom_icon_0f080ebf56e045b88c695028dc6468f8);
        
    
            var marker_1101597701d14582baaae2a78dfef51c = L.marker(
                [-14.7054025, 34.353037],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_011716a008d5430e8d26c8db3b6f6d1e = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_1101597701d14582baaae2a78dfef51c.setIcon(custom_icon_011716a008d5430e8d26c8db3b6f6d1e);
        
    
            var marker_3b7ab1dcd7de4c5b81d1c593327772cd = L.marker(
                [-25.0377998, 33.6273994],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_c83e215897144d5488296bb848a00978 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_3b7ab1dcd7de4c5b81d1c593327772cd.setIcon(custom_icon_c83e215897144d5488296bb848a00978);
        
    
            var marker_2d2d445c226a4119867a16dfde29af40 = L.marker(
                [-21.7080002, 35.4528008],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_0c89ed185f7d4545bb3fdbb162c47539 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_2d2d445c226a4119867a16dfde29af40.setIcon(custom_icon_0c89ed185f7d4545bb3fdbb162c47539);
        
    
            var marker_94aa2a6ba4554f058da0a6da8cb1dabb = L.marker(
                [-13.1218996, 39.0527992],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_d0ec6ad1a4b54a6fba6ac3fec750763b = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_94aa2a6ba4554f058da0a6da8cb1dabb.setIcon(custom_icon_d0ec6ad1a4b54a6fba6ac3fec750763b);
        
    
            var marker_61ae8ef8c507491ab68147d151ac32fb = L.marker(
                [-21.6149998, 35.3380013],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_82a941db48404f79881daf5890e09048 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_61ae8ef8c507491ab68147d151ac32fb.setIcon(custom_icon_82a941db48404f79881daf5890e09048);
        
    
            var marker_599c95b0f2bc43cfb74c9cbe397e5bc7 = L.marker(
                [-19.7997428, 34.9176636],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_4e8820027fea490c920c69609d5af22b = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_599c95b0f2bc43cfb74c9cbe397e5bc7.setIcon(custom_icon_4e8820027fea490c920c69609d5af22b);
        
    
            var marker_d6b2fd0a102748d9abc24eb66ebce4b0 = L.marker(
                [-26.802856, 32.8835637],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_9893a3ef4445480d9f2b530c7b5bb8d4 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_d6b2fd0a102748d9abc24eb66ebce4b0.setIcon(custom_icon_9893a3ef4445480d9f2b530c7b5bb8d4);
        
    
            var marker_052ce0ad0d2743b4b630b1cdb5a049bb = L.marker(
                [-25.0319515, 32.7483858],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_7ecc13df8d3543d09572f50dc86a29c4 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_052ce0ad0d2743b4b630b1cdb5a049bb.setIcon(custom_icon_7ecc13df8d3543d09572f50dc86a29c4);
        
    
            var marker_5f405fe5b5fb4bd48e9ea894422f65ed = L.marker(
                [-22.8208754, 32.0042977],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_a73db77392a34191a3d57918dec4215e = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_5f405fe5b5fb4bd48e9ea894422f65ed.setIcon(custom_icon_a73db77392a34191a3d57918dec4215e);
        
    
            var marker_67d32db2bf714b2cbe1ad44bb0d2d315 = L.marker(
                [-21.5879383, 32.9292169],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_a1793073bd7e4c9fa2e1898ddb4da750 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_67d32db2bf714b2cbe1ad44bb0d2d315.setIcon(custom_icon_a1793073bd7e4c9fa2e1898ddb4da750);
        
    
            var marker_26195827479242d5964a93fd2db970ba = L.marker(
                [-25.2376204, 32.1598927],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_75956e344fb54ff9bbcd13303abd29f3 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_26195827479242d5964a93fd2db970ba.setIcon(custom_icon_75956e344fb54ff9bbcd13303abd29f3);
        
    
            var marker_2f61d23c971244dba90375efa4c81c82 = L.marker(
                [-25.1995933, 33.5011298],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_5725b95ac4f74d3e961458e620368e0e = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_2f61d23c971244dba90375efa4c81c82.setIcon(custom_icon_5725b95ac4f74d3e961458e620368e0e);
        
    
            var marker_8874c5fd4dd044daa7a6555ac71ab1fa = L.marker(
                [-21.7532037, 35.0598754],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_ddba9f5e1fcb448080fbf60927d781d0 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_8874c5fd4dd044daa7a6555ac71ab1fa.setIcon(custom_icon_ddba9f5e1fcb448080fbf60927d781d0);
        
    
            var marker_cfd6b63dac2d4f3783efa7c83a77bf6a = L.marker(
                [-21.5264614, 35.4807876],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_0637c144024444e2b97e56ea4e784f30 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_cfd6b63dac2d4f3783efa7c83a77bf6a.setIcon(custom_icon_0637c144024444e2b97e56ea4e784f30);
        
    
            var marker_cd89aedc8bb742f9a64d8a4002626d1f = L.marker(
                [-12.2005615, 40.5689777],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_62c823a22838450eaed1fa818eade756 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_cd89aedc8bb742f9a64d8a4002626d1f.setIcon(custom_icon_62c823a22838450eaed1fa818eade756);
        
    
            var marker_7801485eac34412e820deffe748e6713 = L.marker(
                [-17.8631466, 36.8702758],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_71cd67de192e4ca19dac173f8689d9bc = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_7801485eac34412e820deffe748e6713.setIcon(custom_icon_71cd67de192e4ca19dac173f8689d9bc);
        
    
            var marker_87883f45f9774b889c81e0c6d704967c = L.marker(
                [-23.9395556, 32.1538495],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_b7809f82bf194b0d8caacf1497415018 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_87883f45f9774b889c81e0c6d704967c.setIcon(custom_icon_b7809f82bf194b0d8caacf1497415018);
        
    
            var marker_a47da563cb774f0a803505cdbd7e4271 = L.marker(
                [-25.309864, 32.2587114],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_3190da2d3c304c15bd4b97e53b472485 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_a47da563cb774f0a803505cdbd7e4271.setIcon(custom_icon_3190da2d3c304c15bd4b97e53b472485);
        
    
            var marker_005988d3220d49108a51baec39ffc4cb = L.marker(
                [-26.0461341, 32.2776677],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_b889fa518159425f8a5021a88b8311a5 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_005988d3220d49108a51baec39ffc4cb.setIcon(custom_icon_b889fa518159425f8a5021a88b8311a5);
        
    
            var marker_53bc2520af11431ebab20d1ba8368877 = L.marker(
                [-12.3501793, 40.6019581],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_05b25e264814424db18d03ab6a5e7b22 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_53bc2520af11431ebab20d1ba8368877.setIcon(custom_icon_05b25e264814424db18d03ab6a5e7b22);
        
    
            var marker_d7e60c7d92884684bd9d4d7019170b64 = L.marker(
                [-14.2110529, 40.6967906],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_5cce561d5cfc4fccb4d5e048a65b7881 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_d7e60c7d92884684bd9d4d7019170b64.setIcon(custom_icon_5cce561d5cfc4fccb4d5e048a65b7881);
        
    
            var marker_5e3f5f5a6dd64720afce45981fddade2 = L.marker(
                [-13.4070995, 39.8028527],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_307add1d5b3744d08cb3279aac4169cd = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_5e3f5f5a6dd64720afce45981fddade2.setIcon(custom_icon_307add1d5b3744d08cb3279aac4169cd);
        
    
            var marker_2ba65ee6ae344308bf1573a3316ce665 = L.marker(
                [-14.8790274, 40.0434146],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_1162c536d36543ef90dd3ecb76d9e5cd = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_2ba65ee6ae344308bf1573a3316ce665.setIcon(custom_icon_1162c536d36543ef90dd3ecb76d9e5cd);
        
    
            var marker_2cf36f436dec4433aaa8093a3c92da7a = L.marker(
                [-15.5040186, 36.98669],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_e65d914a30a6489ab6cd2d2d7af2ca94 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_2cf36f436dec4433aaa8093a3c92da7a.setIcon(custom_icon_e65d914a30a6489ab6cd2d2d7af2ca94);
        
    
            var marker_7e7c67cb3d5344b0bc31e77202bc69ec = L.marker(
                [-15.7363258, 32.762586],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_2c92d5d18c994540bf502784c8092d21 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_7e7c67cb3d5344b0bc31e77202bc69ec.setIcon(custom_icon_2c92d5d18c994540bf502784c8092d21);
        
    
            var marker_edfff071988a446e8b57bd7d866e3a04 = L.marker(
                [-24.2247201, 35.4216259],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_3666710b4e354dc4829f9660b92630c6 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_edfff071988a446e8b57bd7d866e3a04.setIcon(custom_icon_3666710b4e354dc4829f9660b92630c6);
        
    
            var marker_004fbb4a23e74118888f4f31f585f250 = L.marker(
                [-11.3596821, 40.3538089],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_acf677b8746343eeba09a027c4fae707 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_004fbb4a23e74118888f4f31f585f250.setIcon(custom_icon_acf677b8746343eeba09a027c4fae707);
        
    
            var marker_a46d0ec213574f149db9db4648d4c5b9 = L.marker(
                [-10.7524932, 40.47087],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_f15eee4475c340de83ffc66a1a92206a = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_a46d0ec213574f149db9db4648d4c5b9.setIcon(custom_icon_f15eee4475c340de83ffc66a1a92206a);
        
    
            var marker_33fb6eb59fdb439eb718cb42f9824277 = L.marker(
                [-11.9008621, 37.1886348],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_edcadaaa2023485cb1d51d418d11d4f6 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_33fb6eb59fdb439eb718cb42f9824277.setIcon(custom_icon_edcadaaa2023485cb1d51d418d11d4f6);
        
    
            var marker_bf81c4fc7c544578abc97c72915ec718 = L.marker(
                [-12.5498226, 36.2569637],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_58bdbb5b640d45a0b0bb44503fb2b096 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_bf81c4fc7c544578abc97c72915ec718.setIcon(custom_icon_58bdbb5b640d45a0b0bb44503fb2b096);
        
    
            var marker_ae6ea42f76774963a19f22eba9810de5 = L.marker(
                [-11.6412688, 37.1481759],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_02f28123af344997801ea67ba99fa9c8 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_ae6ea42f76774963a19f22eba9810de5.setIcon(custom_icon_02f28123af344997801ea67ba99fa9c8);
        
    
            var marker_9ed24bd859d84c0cbbfbda35464f195e = L.marker(
                [-11.3401855, 38.3030171],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_32bbaff9271944c0b7f49e0ad054ebed = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_9ed24bd859d84c0cbbfbda35464f195e.setIcon(custom_icon_32bbaff9271944c0b7f49e0ad054ebed);
        
    
            var marker_de6d07de78854c8e8ad9f8d4ee053181 = L.marker(
                [-12.6018862, 36.5552365],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_261dcc5bc1ea4bc39d5e76384e878cdb = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_de6d07de78854c8e8ad9f8d4ee053181.setIcon(custom_icon_261dcc5bc1ea4bc39d5e76384e878cdb);
        
    
            var marker_c1455d1595bc4fc8a0956e9bffcab4e2 = L.marker(
                [-12.4660624, 37.6600486],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_677a8d3669a14af4bd1fabf06202cda2 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_c1455d1595bc4fc8a0956e9bffcab4e2.setIcon(custom_icon_677a8d3669a14af4bd1fabf06202cda2);
        
    
            var marker_6dafac4b04404ceb8dacce53058cfcf2 = L.marker(
                [-12.2424529, 38.0001527],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_b37a30756e3841409f43d8005bc7d4eb = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_6dafac4b04404ceb8dacce53058cfcf2.setIcon(custom_icon_b37a30756e3841409f43d8005bc7d4eb);
        
    
            var marker_472b9f052af949aca0b9c0e147bcc1f4 = L.marker(
                [-12.1403522, 38.3189937],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_6086e068337948edbf90859d04c1e68b = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_472b9f052af949aca0b9c0e147bcc1f4.setIcon(custom_icon_6086e068337948edbf90859d04c1e68b);
        
    
            var marker_ae81464a7aea493191117c027a95d91f = L.marker(
                [-12.1515121, 38.2838889],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_e27c687b85b94d658718b44f54a8d77e = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_ae81464a7aea493191117c027a95d91f.setIcon(custom_icon_e27c687b85b94d658718b44f54a8d77e);
        
    
            var marker_a01c1dabbd444ac3a87d7d7f5b8402d8 = L.marker(
                [-12.1696793, 37.54613],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_cd0865877fe14ac6b4fc21d9a5341891 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_a01c1dabbd444ac3a87d7d7f5b8402d8.setIcon(custom_icon_cd0865877fe14ac6b4fc21d9a5341891);
        
    
            var marker_be1e74c54de941b5aeaa827353c28573 = L.marker(
                [-11.0729292, 39.6748264],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_32ecd0b2616c4155837acfcb773e5f81 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_be1e74c54de941b5aeaa827353c28573.setIcon(custom_icon_32ecd0b2616c4155837acfcb773e5f81);
        
    
            var marker_b01bfcb54973459c96cca8db055f724b = L.marker(
                [-17.8636198, 36.8703153],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_5a85cbfb3e124d4a822bab06d0af8b00 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_b01bfcb54973459c96cca8db055f724b.setIcon(custom_icon_5a85cbfb3e124d4a822bab06d0af8b00);
        
    
            var marker_752e7e9991e445db8c7ab1ad9ce2011c = L.marker(
                [-16.1134508, 33.6397552],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_14321d7da18f41fea2236634908d6c52 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_752e7e9991e445db8c7ab1ad9ce2011c.setIcon(custom_icon_14321d7da18f41fea2236634908d6c52);
        
    
            var marker_29953df88208435f8095fe1de3a58f4e = L.marker(
                [-16.113449, 33.6396726],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_e296f8ab267d41aeb9066f3c51b44028 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_29953df88208435f8095fe1de3a58f4e.setIcon(custom_icon_e296f8ab267d41aeb9066f3c51b44028);
        
    
            var marker_b22f6a10cb344707a015cfbbf8942774 = L.marker(
                [-16.1134473, 33.6395895],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_5269b8c1d37c4ca2823ccc8b70fc0e30 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_b22f6a10cb344707a015cfbbf8942774.setIcon(custom_icon_5269b8c1d37c4ca2823ccc8b70fc0e30);
        
    
            var marker_fc98e947580741f8a87b9f78a74023a2 = L.marker(
                [-16.1134454, 33.639501],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_67bb333d6cc14a61ab014db6258ea997 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_fc98e947580741f8a87b9f78a74023a2.setIcon(custom_icon_67bb333d6cc14a61ab014db6258ea997);
        
    
            var marker_ed36395476d44f8f8e6c20577273d757 = L.marker(
                [-16.1134424, 33.6393642],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_772075cef3d0472582d9a0552e37884b = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_ed36395476d44f8f8e6c20577273d757.setIcon(custom_icon_772075cef3d0472582d9a0552e37884b);
        
    
            var marker_143b192662b84f969957f44ab39a10b6 = L.marker(
                [-16.1254926, 33.6398068],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_016767773a1948a1aa35130244712791 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_143b192662b84f969957f44ab39a10b6.setIcon(custom_icon_016767773a1948a1aa35130244712791);
        
    
            var marker_ae9cc3db60a74c4385c3c91ddffcdd6d = L.marker(
                [-15.1999937, 35.8695997],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_6423972fda344de0a7ed3729be71a706 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_ae9cc3db60a74c4385c3c91ddffcdd6d.setIcon(custom_icon_6423972fda344de0a7ed3729be71a706);
        
    
            var marker_3ac5f0294cd34b6b94a8d8f7656d16fe = L.marker(
                [-12.7015132, 34.8043578],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_cf0a8e57682a4025be6863f85f9173f1 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_3ac5f0294cd34b6b94a8d8f7656d16fe.setIcon(custom_icon_cf0a8e57682a4025be6863f85f9173f1);
        
    
            var marker_1da5aa1fdc8e43b8a8bb000b7aa54816 = L.marker(
                [-26.3936269, 32.6508692],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_77a20147f4934f25b2b7b4588159eb7c = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_1da5aa1fdc8e43b8a8bb000b7aa54816.setIcon(custom_icon_77a20147f4934f25b2b7b4588159eb7c);
        
    
            var marker_86b046b67759469b83c04d13f7a9e28e = L.marker(
                [-19.8933436, 34.5856456],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_ed2cedbe2ab94d179747c996eb8ff7ac = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_86b046b67759469b83c04d13f7a9e28e.setIcon(custom_icon_ed2cedbe2ab94d179747c996eb8ff7ac);
        
    
            var marker_3df587e25f7f4a6793825b4e33e0b400 = L.marker(
                [-19.7952029, 34.896896],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_ba963fff10ca4b3fa1a7dcefa40cdf81 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_3df587e25f7f4a6793825b4e33e0b400.setIcon(custom_icon_ba963fff10ca4b3fa1a7dcefa40cdf81);
        
    
            var marker_fd9ba120426b44518d3e4da886a45ec7 = L.marker(
                [-19.7999018, 34.9182957],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_5316e855c07b4700aafa9de6644f7563 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_fd9ba120426b44518d3e4da886a45ec7.setIcon(custom_icon_5316e855c07b4700aafa9de6644f7563);
        
    
            var marker_c9cad3433b7b41afabecc155c548cea7 = L.marker(
                [-19.7935243, 34.8993105],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_a24f1bebe81b41e4aa885c3ef5731801 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_c9cad3433b7b41afabecc155c548cea7.setIcon(custom_icon_a24f1bebe81b41e4aa885c3ef5731801);
        
    
            var marker_d722873bd996402991aac1791fef4368 = L.marker(
                [-19.7976317, 34.9061903],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_0e94f9c14afa403dbf0cad1473546995 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_d722873bd996402991aac1791fef4368.setIcon(custom_icon_0e94f9c14afa403dbf0cad1473546995);
        
    
            var marker_cd801bdf4b3b45eea1de435045a8cd1c = L.marker(
                [-19.7995068, 34.9155539],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_c5cae7ac5ce547e38cea84d50e908758 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_cd801bdf4b3b45eea1de435045a8cd1c.setIcon(custom_icon_c5cae7ac5ce547e38cea84d50e908758);
        
    
            var marker_307729134bce4697bcf6a2ef793211c5 = L.marker(
                [-19.799879, 34.9214199],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_3e559678f0044f8c9760eee88903a293 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_307729134bce4697bcf6a2ef793211c5.setIcon(custom_icon_3e559678f0044f8c9760eee88903a293);
        
    
            var marker_5f22eacfc6cf4885a8a7e12c396201a2 = L.marker(
                [-19.796438, 34.9045864],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_c7d49d2189db44309ef99c9050d2d964 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_5f22eacfc6cf4885a8a7e12c396201a2.setIcon(custom_icon_c7d49d2189db44309ef99c9050d2d964);
        
    
            var marker_681f330f724f43a5b78cdfffc3ccabc0 = L.marker(
                [-17.8501549, 36.8689343],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_55c504f118e04cd3a017d264502f2f4b = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_681f330f724f43a5b78cdfffc3ccabc0.setIcon(custom_icon_55c504f118e04cd3a017d264502f2f4b);
        
    
            var marker_241337e99c9f4e36aaa7b204c9c5e7ed = L.marker(
                [-17.8587714, 36.8698007],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_27ff966baf944bdc8b8eed69d2ba7daf = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_241337e99c9f4e36aaa7b204c9c5e7ed.setIcon(custom_icon_27ff966baf944bdc8b8eed69d2ba7daf);
        
    
            var marker_1d38f9cffef349f1a391cfc263fbc12c = L.marker(
                [-19.1489727, 33.4278915],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_1ebb37e2166e441e84a5fb1b4f0dcb4d = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_1d38f9cffef349f1a391cfc263fbc12c.setIcon(custom_icon_1ebb37e2166e441e84a5fb1b4f0dcb4d);
        
    
            var marker_8bd59473d2cb41319e0f8d3124de74a7 = L.marker(
                [-19.1479985, 33.4282918],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_1e2850ef8d8c449588afffe2f6dc9ef7 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_8bd59473d2cb41319e0f8d3124de74a7.setIcon(custom_icon_1e2850ef8d8c449588afffe2f6dc9ef7);
        
    
            var marker_9d4f37b439254c83a89fc1a19fbc72f5 = L.marker(
                [-19.1499533, 33.4281135],
                {"iconSize": [14, 14]}
            ).addTo(map_908d913a32b24391b93547490dfdad73);
        
    
        var custom_icon_496f8d75543a43c2b5a84bca176a0126 = L.icon({"iconSize": [14, 14], "iconUrl": "https://static.thenounproject.com/png/2009208-200.png"});
        marker_9d4f37b439254c83a89fc1a19fbc72f5.setIcon(custom_icon_496f8d75543a43c2b5a84bca176a0126);
        
</script>