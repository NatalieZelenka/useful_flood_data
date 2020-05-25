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
                #map_f36c66056d4d43709c3d5f32961f15c8 {
                    position: relative;
                    width: 100.0%;
                    height: 100.0%;
                    left: 0.0%;
                    top: 0.0%;
                }
            </style>
        
</head>
<body>    
    
            <div class="folium-map" id="map_f36c66056d4d43709c3d5f32961f15c8" ></div>
        
</body>
<script>    
    
            var map_f36c66056d4d43709c3d5f32961f15c8 = L.map(
                "map_f36c66056d4d43709c3d5f32961f15c8",
                {
                    center: [-16.75, 36.5],
                    crs: L.CRS.EPSG3857,
                    maxBounds: [[-25.0, 30.0], [-8.5, 43.0]],
                    zoom: 10,
                    zoomControl: true,
                    preferCanvas: false,
                }
            );

            

        
    
            var tile_layer_a9e03072212a4f29b737739f1525803c = L.tileLayer(
                "https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png",
                {"attribution": "\u003ca href=\"https://www.openstreetmap.org/copyright\"\u003eOpenStreetMap\u003c/a\u003e contributors, Tiles style by \u003ca href=\"https://www.hotosm.org/\" target=\"_blank\"\u003eHumanitarian OpenStreetMap Team\u003c/a\u003e hosted by \u003ca href=\"https://openstreetmap.fr/\" target=\"_blank\"\u003eOpenStreetMap France\u003c/a\u003e).", "detectRetina": false, "maxNativeZoom": 18, "maxZoom": 18, "minZoom": 5, "noWrap": false, "opacity": 1, "subdomains": "abc", "tms": false}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
            map_f36c66056d4d43709c3d5f32961f15c8.fitBounds(
                [[-25.0, 30.0], [-8.5, 43.0]],
                {}
            );
        
    
            var marker_7ecd119d09314499bbeee5e9eca975fb = L.marker(
                [-16.8536831, 36.966587],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_e086c240bdc64a71ba867c49bd9ec79f = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_7ecd119d09314499bbeee5e9eca975fb.setIcon(custom_icon_e086c240bdc64a71ba867c49bd9ec79f);
        
    
            var marker_1f18e7074af246a8a725a35226ed4a3c = L.marker(
                [-13.2721452, 35.2640604],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_f2fb2bddec9d427a8fe963d3cafaa131 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_1f18e7074af246a8a725a35226ed4a3c.setIcon(custom_icon_f2fb2bddec9d427a8fe963d3cafaa131);
        
    
            var marker_c1802e72109d4056ad24f6332a88dc52 = L.marker(
                [-21.5362894, 35.4731954],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_0cebd51e7e45471faf9e99038e093fda = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_c1802e72109d4056ad24f6332a88dc52.setIcon(custom_icon_0cebd51e7e45471faf9e99038e093fda);
        
    
            var marker_325a38d165f7458daed8c8b668734491 = L.marker(
                [-21.1625508, 34.5610696],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_622614c6b82e486da8bd48b83376e9d1 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_325a38d165f7458daed8c8b668734491.setIcon(custom_icon_622614c6b82e486da8bd48b83376e9d1);
        
    
            var marker_9e141a24c24247dabd84f1321f428635 = L.marker(
                [-25.2659855, 33.2385979],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ff9b13d8112642a2a128ae78bd71fef3 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_9e141a24c24247dabd84f1321f428635.setIcon(custom_icon_ff9b13d8112642a2a128ae78bd71fef3);
        
    
            var marker_f03006039776456c95ea2b488b8f4079 = L.marker(
                [-14.8159887, 36.5316201],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_1c21fffcdb024c42a1e338e6a6582e6d = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_f03006039776456c95ea2b488b8f4079.setIcon(custom_icon_1c21fffcdb024c42a1e338e6a6582e6d);
        
    
            var marker_bbaee72db0374cdda8f6c68393b181ef = L.marker(
                [-25.9971447, 32.9293518],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_d4c543085102463691ce8a7d8aad80b3 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_bbaee72db0374cdda8f6c68393b181ef.setIcon(custom_icon_d4c543085102463691ce8a7d8aad80b3);
        
    
            var marker_6c9c3bd24c8446cf93d843c0dfddd61e = L.marker(
                [-11.6729002, 39.5630989],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a0454c39464c4ba1a92946ad3154051d = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_6c9c3bd24c8446cf93d843c0dfddd61e.setIcon(custom_icon_a0454c39464c4ba1a92946ad3154051d);
        
    
            var marker_a0c1b4ee736d4888abc76f8ea61fae4e = L.marker(
                [-26.8285522, 32.8377075],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_c3d399ee4ffb45b0ac93955cf327dcf2 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_a0c1b4ee736d4888abc76f8ea61fae4e.setIcon(custom_icon_c3d399ee4ffb45b0ac93955cf327dcf2);
        
    
            var marker_2fed637f0d184f928a73ebb9cf6d7450 = L.marker(
                [-15.6027002, 32.773201],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_e20efe6cc9a04e09befe360af61aeb57 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_2fed637f0d184f928a73ebb9cf6d7450.setIcon(custom_icon_e20efe6cc9a04e09befe360af61aeb57);
        
    
            var marker_68ebe807df0d4c35827e34c898867e34 = L.marker(
                [-14.7054025, 34.353037],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_f647d2a7397346a38ad37dd8e5a48257 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_68ebe807df0d4c35827e34c898867e34.setIcon(custom_icon_f647d2a7397346a38ad37dd8e5a48257);
        
    
            var marker_15c72c5217174624a8b8981b0679a737 = L.marker(
                [-25.0377998, 33.6273994],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_d6a921053f50421a8a95daf001870a3d = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_15c72c5217174624a8b8981b0679a737.setIcon(custom_icon_d6a921053f50421a8a95daf001870a3d);
        
    
            var marker_a38bf632fff546abbb9877932976eddf = L.marker(
                [-21.7080002, 35.4528008],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_e603f65c64c147c59081eb8050cf80f3 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_a38bf632fff546abbb9877932976eddf.setIcon(custom_icon_e603f65c64c147c59081eb8050cf80f3);
        
    
            var marker_970295c4ab714b66bf145fd4791974f8 = L.marker(
                [-13.1218996, 39.0527992],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_e85f4f0207a2454a83021929ebb64c1d = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_970295c4ab714b66bf145fd4791974f8.setIcon(custom_icon_e85f4f0207a2454a83021929ebb64c1d);
        
    
            var marker_67f743efc121421c9d77ed21c7d9f390 = L.marker(
                [-21.6149998, 35.3380013],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_6ad917fc7822485c83603525466addfa = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_67f743efc121421c9d77ed21c7d9f390.setIcon(custom_icon_6ad917fc7822485c83603525466addfa);
        
    
            var marker_f3d9a172db4a40378a565bf186ce847c = L.marker(
                [-19.7997428, 34.9176636],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_e0337512b9e245048b702a209db5a525 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_f3d9a172db4a40378a565bf186ce847c.setIcon(custom_icon_e0337512b9e245048b702a209db5a525);
        
    
            var marker_f3fa36321811480e83288ee1c21551a0 = L.marker(
                [-26.802856, 32.8835637],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_0f385be7c16b41cc91f573cd93dc5eaa = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_f3fa36321811480e83288ee1c21551a0.setIcon(custom_icon_0f385be7c16b41cc91f573cd93dc5eaa);
        
    
            var marker_52a97e0d6c324a008490d7f805b92927 = L.marker(
                [-25.0319515, 32.7483858],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_e41597c0f99d45e1ab062fefea71b5a5 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_52a97e0d6c324a008490d7f805b92927.setIcon(custom_icon_e41597c0f99d45e1ab062fefea71b5a5);
        
    
            var marker_493732ec50b547f5a1d74b07c0a4ab9c = L.marker(
                [-22.8208754, 32.0042977],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_7dec21a6be8842e09b7f45536094e278 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_493732ec50b547f5a1d74b07c0a4ab9c.setIcon(custom_icon_7dec21a6be8842e09b7f45536094e278);
        
    
            var marker_300a65b0729d433b84e62721cbeec1b1 = L.marker(
                [-21.5879383, 32.9292169],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_fc1cf0ad09bc47cf8ee22a440af3cadd = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_300a65b0729d433b84e62721cbeec1b1.setIcon(custom_icon_fc1cf0ad09bc47cf8ee22a440af3cadd);
        
    
            var marker_5d988d55ea5c446294272f4b9831103d = L.marker(
                [-25.2376204, 32.1598927],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_b27bf170e6114f67b4be4c131e3fb230 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_5d988d55ea5c446294272f4b9831103d.setIcon(custom_icon_b27bf170e6114f67b4be4c131e3fb230);
        
    
            var marker_40bfcfdf6a1c4c3181f49d3ce113b28b = L.marker(
                [-25.1995933, 33.5011298],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_d68032f0ced54cd7977afd2717d77f67 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_40bfcfdf6a1c4c3181f49d3ce113b28b.setIcon(custom_icon_d68032f0ced54cd7977afd2717d77f67);
        
    
            var marker_9cdace73b6a141a49d5408935d5a7618 = L.marker(
                [-21.7532037, 35.0598754],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_2f9105da45614ca29a08f3e5e80fdd53 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_9cdace73b6a141a49d5408935d5a7618.setIcon(custom_icon_2f9105da45614ca29a08f3e5e80fdd53);
        
    
            var marker_ac33c930b88f429bbb261610742ee57a = L.marker(
                [-21.5264614, 35.4807876],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ee4fdc3b5b8f4dfc99abbd3a34cad4b4 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_ac33c930b88f429bbb261610742ee57a.setIcon(custom_icon_ee4fdc3b5b8f4dfc99abbd3a34cad4b4);
        
    
            var marker_0a6aac657cbb4342bcb5b5e45bbf0cfc = L.marker(
                [-12.2005615, 40.5689777],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a63a1b89a5ef45d2b4df295ee72db334 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_0a6aac657cbb4342bcb5b5e45bbf0cfc.setIcon(custom_icon_a63a1b89a5ef45d2b4df295ee72db334);
        
    
            var marker_d2fc791617f943c38b4d9912f01ecf3b = L.marker(
                [-17.8631466, 36.8702758],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_3480ec2ca08449b0ae17043d97859f2f = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_d2fc791617f943c38b4d9912f01ecf3b.setIcon(custom_icon_3480ec2ca08449b0ae17043d97859f2f);
        
    
            var marker_a73a94733e154759b5639e99495a7721 = L.marker(
                [-23.9395556, 32.1538495],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_f5dac573e8dd4be98b5f6a926caa1364 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_a73a94733e154759b5639e99495a7721.setIcon(custom_icon_f5dac573e8dd4be98b5f6a926caa1364);
        
    
            var marker_20933ba0d7244d1e9599b4c427e6fbf2 = L.marker(
                [-25.309864, 32.2587114],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_5956d455415d46958340a6bdd6e4b5b7 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_20933ba0d7244d1e9599b4c427e6fbf2.setIcon(custom_icon_5956d455415d46958340a6bdd6e4b5b7);
        
    
            var marker_5e49204b2d31461dbf54f31f1dc003b5 = L.marker(
                [-26.0461341, 32.2776677],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_1202e5f1a59a400d92b8329643c6dfdd = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_5e49204b2d31461dbf54f31f1dc003b5.setIcon(custom_icon_1202e5f1a59a400d92b8329643c6dfdd);
        
    
            var marker_f23731fa8aa24649a0abb6862affb8b3 = L.marker(
                [-12.3501793, 40.6019581],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_c2927513c69749b38b87a929d7d95208 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_f23731fa8aa24649a0abb6862affb8b3.setIcon(custom_icon_c2927513c69749b38b87a929d7d95208);
        
    
            var marker_d5d3cecefa7f4c6c9dde30316523b090 = L.marker(
                [-14.2110529, 40.6967906],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_e7672f6ba007407c9df909f665928dd7 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_d5d3cecefa7f4c6c9dde30316523b090.setIcon(custom_icon_e7672f6ba007407c9df909f665928dd7);
        
    
            var marker_44a638589fe548e598a570ed1687f799 = L.marker(
                [-13.4070995, 39.8028527],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_6e4400dd613844468951045533e3ba63 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_44a638589fe548e598a570ed1687f799.setIcon(custom_icon_6e4400dd613844468951045533e3ba63);
        
    
            var marker_56196af4ef8747739ed73baf6ba3ec5c = L.marker(
                [-14.8790274, 40.0434146],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_282f06ce695d4581968549318a3fc9ae = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_56196af4ef8747739ed73baf6ba3ec5c.setIcon(custom_icon_282f06ce695d4581968549318a3fc9ae);
        
    
            var marker_5c250c4f0934449988863c4e0aaeda44 = L.marker(
                [-15.5040186, 36.98669],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_52e26dfa80bf408d823aa755b1809ef3 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_5c250c4f0934449988863c4e0aaeda44.setIcon(custom_icon_52e26dfa80bf408d823aa755b1809ef3);
        
    
            var marker_feb74e41bfb846139b4657e7dff75ba2 = L.marker(
                [-15.7363258, 32.762586],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a6fe38ac2553406e8cde890881a84e89 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_feb74e41bfb846139b4657e7dff75ba2.setIcon(custom_icon_a6fe38ac2553406e8cde890881a84e89);
        
    
            var marker_e7d6ea22336f467a95a3e6e79461cdb0 = L.marker(
                [-24.2247201, 35.4216259],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_df84914d94034386b97f2dee57d73341 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_e7d6ea22336f467a95a3e6e79461cdb0.setIcon(custom_icon_df84914d94034386b97f2dee57d73341);
        
    
            var marker_a1aef7063187428c957c1cf247243725 = L.marker(
                [-11.3596821, 40.3538089],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_f052de4b968745abbdf5165d2f68cc5f = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_a1aef7063187428c957c1cf247243725.setIcon(custom_icon_f052de4b968745abbdf5165d2f68cc5f);
        
    
            var marker_9345fb4aa1894b648d1c2f3c4017af61 = L.marker(
                [-10.7524932, 40.47087],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_318e88203e2a4838b445907441d8d47c = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_9345fb4aa1894b648d1c2f3c4017af61.setIcon(custom_icon_318e88203e2a4838b445907441d8d47c);
        
    
            var marker_70867a70ac26455283d7543e632e0e88 = L.marker(
                [-11.9008621, 37.1886348],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_5d94ab24cd16405793baac2a472c3820 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_70867a70ac26455283d7543e632e0e88.setIcon(custom_icon_5d94ab24cd16405793baac2a472c3820);
        
    
            var marker_4f1ca58683b548fb96ab61ceb3ff3504 = L.marker(
                [-12.5498226, 36.2569637],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ae928c813c214262942898b462344652 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_4f1ca58683b548fb96ab61ceb3ff3504.setIcon(custom_icon_ae928c813c214262942898b462344652);
        
    
            var marker_d4b1a659756340f19f223b05d436d667 = L.marker(
                [-11.6412688, 37.1481759],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_9872a6fa07884949a98120716fe2d1e0 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_d4b1a659756340f19f223b05d436d667.setIcon(custom_icon_9872a6fa07884949a98120716fe2d1e0);
        
    
            var marker_8bb5128af8ce4b6f8ddad1ce23155399 = L.marker(
                [-11.3401855, 38.3030171],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_14e643be9b1f4ef980695ff7aef6a84f = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_8bb5128af8ce4b6f8ddad1ce23155399.setIcon(custom_icon_14e643be9b1f4ef980695ff7aef6a84f);
        
    
            var marker_f1f16e7d1ade451db5aad69b8a35750c = L.marker(
                [-12.6018862, 36.5552365],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_5a5e8a46708c4e81a8243a6887d514fa = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_f1f16e7d1ade451db5aad69b8a35750c.setIcon(custom_icon_5a5e8a46708c4e81a8243a6887d514fa);
        
    
            var marker_ba5a85bea865485d982fd50efa60b84d = L.marker(
                [-12.4660624, 37.6600486],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_8d21c22f2edd4e07b12056e04c0309a8 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_ba5a85bea865485d982fd50efa60b84d.setIcon(custom_icon_8d21c22f2edd4e07b12056e04c0309a8);
        
    
            var marker_68e96d26660e4075a009e3e19efeb2a1 = L.marker(
                [-12.2424529, 38.0001527],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_76f8ddf6202e4b10bbcef397f5596520 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_68e96d26660e4075a009e3e19efeb2a1.setIcon(custom_icon_76f8ddf6202e4b10bbcef397f5596520);
        
    
            var marker_ffa054d916c84f98a91dba6ea7f968e1 = L.marker(
                [-12.1403522, 38.3189937],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_977f2ace2f5144c589a2fbc3914b7b24 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_ffa054d916c84f98a91dba6ea7f968e1.setIcon(custom_icon_977f2ace2f5144c589a2fbc3914b7b24);
        
    
            var marker_527a36eb80ca4625b07c1524bd429545 = L.marker(
                [-12.1515121, 38.2838889],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a47aac0b990948f7b8ba6e694c0b8c63 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_527a36eb80ca4625b07c1524bd429545.setIcon(custom_icon_a47aac0b990948f7b8ba6e694c0b8c63);
        
    
            var marker_79ca06e346fe4303b00dcfdc92f1143f = L.marker(
                [-12.1696793, 37.54613],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_5d3e8931f82e425fbfb72b90cd2a63e2 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_79ca06e346fe4303b00dcfdc92f1143f.setIcon(custom_icon_5d3e8931f82e425fbfb72b90cd2a63e2);
        
    
            var marker_550be1a05e534ac8b2fb7fd7957e8781 = L.marker(
                [-11.0729292, 39.6748264],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_2450be8423314d0f9338a4c00463bddf = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_550be1a05e534ac8b2fb7fd7957e8781.setIcon(custom_icon_2450be8423314d0f9338a4c00463bddf);
        
    
            var marker_becf05cced6d47f884c8074b93924ffd = L.marker(
                [-17.8636198, 36.8703153],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_6992ea7e735e47fe908c1e93c6f81e06 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_becf05cced6d47f884c8074b93924ffd.setIcon(custom_icon_6992ea7e735e47fe908c1e93c6f81e06);
        
    
            var marker_4bfa3277da0447f694e534e14821ea0e = L.marker(
                [-16.1134508, 33.6397552],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_39d3114fc31b4d5789e8c4b7439ca62d = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_4bfa3277da0447f694e534e14821ea0e.setIcon(custom_icon_39d3114fc31b4d5789e8c4b7439ca62d);
        
    
            var marker_8b89a833a7bb4f31b61465dec811c2aa = L.marker(
                [-16.113449, 33.6396726],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_fe1ac7db7847464f888ef2f5031be3d1 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_8b89a833a7bb4f31b61465dec811c2aa.setIcon(custom_icon_fe1ac7db7847464f888ef2f5031be3d1);
        
    
            var marker_065906b6209143f09e3ce57d64e305e7 = L.marker(
                [-16.1134473, 33.6395895],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_87f67145606c422e977c9bd7c34ccd4d = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_065906b6209143f09e3ce57d64e305e7.setIcon(custom_icon_87f67145606c422e977c9bd7c34ccd4d);
        
    
            var marker_0b1c2820c7784a8bb19316de8dcfe988 = L.marker(
                [-16.1134454, 33.639501],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_eeb620289ec645879c3fa91e9df03b43 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_0b1c2820c7784a8bb19316de8dcfe988.setIcon(custom_icon_eeb620289ec645879c3fa91e9df03b43);
        
    
            var marker_40c6c780c78f4a8288ea9151133d37c1 = L.marker(
                [-16.1134424, 33.6393642],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_928effa05eea4571b88e1c404bb6461c = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_40c6c780c78f4a8288ea9151133d37c1.setIcon(custom_icon_928effa05eea4571b88e1c404bb6461c);
        
    
            var marker_99a0077b15b243c49096b7e8c3dbc476 = L.marker(
                [-16.1254926, 33.6398068],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_495a803ff6e9477382ff914050603616 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_99a0077b15b243c49096b7e8c3dbc476.setIcon(custom_icon_495a803ff6e9477382ff914050603616);
        
    
            var marker_ce33c18339944f728e1dd301cdc0ef54 = L.marker(
                [-15.1999937, 35.8695997],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_468950b6012c4d94ab36865e0d6f81bf = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_ce33c18339944f728e1dd301cdc0ef54.setIcon(custom_icon_468950b6012c4d94ab36865e0d6f81bf);
        
    
            var marker_867b251f3c2f4a948f48c40297eacfba = L.marker(
                [-12.7015132, 34.8043578],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_34be75c5bde74f1d92d4dee2c976ab15 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_867b251f3c2f4a948f48c40297eacfba.setIcon(custom_icon_34be75c5bde74f1d92d4dee2c976ab15);
        
    
            var marker_7c9ee3cc987348e1a25c9445129e97c1 = L.marker(
                [-26.3936269, 32.6508692],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_889a76713bf4437abd4c77d73a2a28cc = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_7c9ee3cc987348e1a25c9445129e97c1.setIcon(custom_icon_889a76713bf4437abd4c77d73a2a28cc);
        
    
            var marker_b79f1d8b699a49b6bab21d92d19a5a7e = L.marker(
                [-19.8933436, 34.5856456],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_bf00feb0b8a84b3287ed695f026b3ec3 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_b79f1d8b699a49b6bab21d92d19a5a7e.setIcon(custom_icon_bf00feb0b8a84b3287ed695f026b3ec3);
        
    
            var marker_63808e8adf0b447e92869a6d71ed2baa = L.marker(
                [-19.7952029, 34.896896],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_556640eae7a84bffa1a64aff25efd389 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_63808e8adf0b447e92869a6d71ed2baa.setIcon(custom_icon_556640eae7a84bffa1a64aff25efd389);
        
    
            var marker_a48ada44b75a47d1aa1af95cecc8270e = L.marker(
                [-19.7999018, 34.9182957],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_9c4df0fb6d344e498c9918d8f6e0d423 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_a48ada44b75a47d1aa1af95cecc8270e.setIcon(custom_icon_9c4df0fb6d344e498c9918d8f6e0d423);
        
    
            var marker_2e6542c1709144c2a8096b38573acdb1 = L.marker(
                [-19.7935243, 34.8993105],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_4ee4438806fb45bc90e3aa1f670fe6a0 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_2e6542c1709144c2a8096b38573acdb1.setIcon(custom_icon_4ee4438806fb45bc90e3aa1f670fe6a0);
        
    
            var marker_9504cbefc5d4470a90b3bd40b42b9dc2 = L.marker(
                [-19.7976317, 34.9061903],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_7703d5ee78824b8185c4bc0b573130ec = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_9504cbefc5d4470a90b3bd40b42b9dc2.setIcon(custom_icon_7703d5ee78824b8185c4bc0b573130ec);
        
    
            var marker_5dbe62ca7a9b4671b692d93caddc9a2b = L.marker(
                [-19.7995068, 34.9155539],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_49813a3318f847808bab175ec7fccb65 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_5dbe62ca7a9b4671b692d93caddc9a2b.setIcon(custom_icon_49813a3318f847808bab175ec7fccb65);
        
    
            var marker_13fdf1cacebd41c1bff080c23090948f = L.marker(
                [-19.799879, 34.9214199],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a14750ddec4d4fd98644c90a8b2285c6 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_13fdf1cacebd41c1bff080c23090948f.setIcon(custom_icon_a14750ddec4d4fd98644c90a8b2285c6);
        
    
            var marker_0056ed5abe77491bb64ee9f702c052a0 = L.marker(
                [-19.796438, 34.9045864],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_664e05c77dfd431f9bce7c4cc1de84a0 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_0056ed5abe77491bb64ee9f702c052a0.setIcon(custom_icon_664e05c77dfd431f9bce7c4cc1de84a0);
        
    
            var marker_59c5da21cf2147bcb99233f4604fb7b9 = L.marker(
                [-17.8501549, 36.8689343],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_bcff7fb2d85746279ab4f99ff4d6ec7e = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_59c5da21cf2147bcb99233f4604fb7b9.setIcon(custom_icon_bcff7fb2d85746279ab4f99ff4d6ec7e);
        
    
            var marker_cd473a25a2f941c38e08bfdcd60d1779 = L.marker(
                [-17.8587714, 36.8698007],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_0686d002f8214a6886dedc5884dc66e6 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_cd473a25a2f941c38e08bfdcd60d1779.setIcon(custom_icon_0686d002f8214a6886dedc5884dc66e6);
        
    
            var marker_f073bb4e02654a908e38e826eaca8f42 = L.marker(
                [-19.1489727, 33.4278915],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_2612eeb419e04bae9a38930ae021c3e0 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_f073bb4e02654a908e38e826eaca8f42.setIcon(custom_icon_2612eeb419e04bae9a38930ae021c3e0);
        
    
            var marker_78ba80fae6624c85a98abd6b8b636d76 = L.marker(
                [-19.1479985, 33.4282918],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_e901a31cfa2d4928a6f875457d393180 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_78ba80fae6624c85a98abd6b8b636d76.setIcon(custom_icon_e901a31cfa2d4928a6f875457d393180);
        
    
            var marker_80ac00bc04b44d1abbedc241810fca47 = L.marker(
                [-19.1499533, 33.4281135],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_8d167b83c28640b8a58ac84b9bd8eab9 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/airport.svg"});
        marker_80ac00bc04b44d1abbedc241810fca47.setIcon(custom_icon_8d167b83c28640b8a58ac84b9bd8eab9);
        
    
            var marker_42818a7aa08449cab720728cac625d38 = L.marker(
                [-19.8508191, 34.8740248],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_4070408691b54ac48ff021634f1b8ad0 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_42818a7aa08449cab720728cac625d38.setIcon(custom_icon_4070408691b54ac48ff021634f1b8ad0);
        
    
            var marker_466c0ba6d72248df8ac94354d428f93d = L.marker(
                [-19.8202962, 33.9852423],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_3b5859b6c9e647318cde31f373e55fa6 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_466c0ba6d72248df8ac94354d428f93d.setIcon(custom_icon_3b5859b6c9e647318cde31f373e55fa6);
        
    
            var marker_7c1e1fd7c4e44dcea2e66bf4c911d0b5 = L.marker(
                [-23.3317757, 35.3862932],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_b51929178ace4d89a1e253b9a5392b1a = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_7c1e1fd7c4e44dcea2e66bf4c911d0b5.setIcon(custom_icon_b51929178ace4d89a1e253b9a5392b1a);
        
    
            var marker_ac6c38e772864e11b3679fafdc40da4d = L.marker(
                [-23.863515, 35.384746],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_797edc6a907a4c80aaf5ceaa55176baa = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_ac6c38e772864e11b3679fafdc40da4d.setIcon(custom_icon_797edc6a907a4c80aaf5ceaa55176baa);
        
    
            var marker_9292b1a8970f4848b398478cf5000d05 = L.marker(
                [-25.9593111, 32.5961269],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_c45dcae88cc740abbfa2853106c9ce58 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_9292b1a8970f4848b398478cf5000d05.setIcon(custom_icon_c45dcae88cc740abbfa2853106c9ce58);
        
    
            var marker_b8de5ff22a174a7984f4c712307baf67 = L.marker(
                [-25.9557165, 32.6046652],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_3f150b825b894f5db400ab1358e92a19 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_b8de5ff22a174a7984f4c712307baf67.setIcon(custom_icon_3f150b825b894f5db400ab1358e92a19);
        
    
            var marker_be9d2e793c274a60a1a401e14777a9b6 = L.marker(
                [-25.9549448, 32.5886257],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a7a7bd6622ca40b0b3b8dd65df957ec1 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_be9d2e793c274a60a1a401e14777a9b6.setIcon(custom_icon_a7a7bd6622ca40b0b3b8dd65df957ec1);
        
    
            var marker_b3c6d684ad1643ba8b86b2d18842b66c = L.marker(
                [-25.9426735, 32.6113171],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_d5a79e907c5a44fb8625aa2f769dd624 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_b3c6d684ad1643ba8b86b2d18842b66c.setIcon(custom_icon_d5a79e907c5a44fb8625aa2f769dd624);
        
    
            var marker_13f5ddfcdbef4e2a89ee11dc95acb445 = L.marker(
                [-21.539288, 35.1886189],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_8b0a8a3932c147cabece87e0fafbd8c9 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_13f5ddfcdbef4e2a89ee11dc95acb445.setIcon(custom_icon_8b0a8a3932c147cabece87e0fafbd8c9);
        
    
            var marker_afa47d41c53345e3baf69a4240afeca4 = L.marker(
                [-21.9942771, 35.3199865],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_25066422db9d4a8a91390d6ec96f0dfb = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_afa47d41c53345e3baf69a4240afeca4.setIcon(custom_icon_25066422db9d4a8a91390d6ec96f0dfb);
        
    
            var marker_cba469bf70f44a6a956611d0247200a7 = L.marker(
                [-24.530801, 33.0003303],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_7482ba47f6664b93af11e51ec0b1354d = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_cba469bf70f44a6a956611d0247200a7.setIcon(custom_icon_7482ba47f6664b93af11e51ec0b1354d);
        
    
            var marker_3a8ba1eeafd74f2e9844e81448f8a705 = L.marker(
                [-16.1548038, 33.5833747],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_27de6b5e746845a49984ad3e2b3233f2 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_3a8ba1eeafd74f2e9844e81448f8a705.setIcon(custom_icon_27de6b5e746845a49984ad3e2b3233f2);
        
    
            var marker_512014aebe1f48ad8937755782fe0e70 = L.marker(
                [-16.1597692, 33.5867576],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_1734ced1fc0b484d9ce1c9af0bb9f8b1 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_512014aebe1f48ad8937755782fe0e70.setIcon(custom_icon_1734ced1fc0b484d9ce1c9af0bb9f8b1);
        
    
            var marker_66f1cc5300b84b8b90f7b89c7dd91208 = L.marker(
                [-16.1594265, 33.5839707],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_88225d666c604f72893ad83c56cc9f03 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_66f1cc5300b84b8b90f7b89c7dd91208.setIcon(custom_icon_88225d666c604f72893ad83c56cc9f03);
        
    
            var marker_2896fb71d79c443894d2903b28c7f001 = L.marker(
                [-25.9649838, 32.5917064],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_f30bac98091f4851b2667dc30d358cb8 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_2896fb71d79c443894d2903b28c7f001.setIcon(custom_icon_f30bac98091f4851b2667dc30d358cb8);
        
    
            var marker_6e64e4e437e34209b9921820e0778ac7 = L.marker(
                [-25.9666709, 32.595576],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a4af2134ce694bc39db64c2e808d5acf = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_6e64e4e437e34209b9921820e0778ac7.setIcon(custom_icon_a4af2134ce694bc39db64c2e808d5acf);
        
    
            var marker_118712ab68704908ac217cc12087f75b = L.marker(
                [-25.9712374, 32.5766384],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_4a57a2d655e7499881e78fc04cc32a68 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_118712ab68704908ac217cc12087f75b.setIcon(custom_icon_4a57a2d655e7499881e78fc04cc32a68);
        
    
            var marker_af431d7dca3e4027a075b89cdfb7d565 = L.marker(
                [-25.9744278, 32.5937832],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_8f2cb1fa79d94ad6a55bc379b2c15507 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_af431d7dca3e4027a075b89cdfb7d565.setIcon(custom_icon_8f2cb1fa79d94ad6a55bc379b2c15507);
        
    
            var marker_2d42ba32c90d4612a897e6a6fe4aa074 = L.marker(
                [-23.8549449, 35.5462025],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_6989903e3d94433bae8efee3fc12c02c = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_2d42ba32c90d4612a897e6a6fe4aa074.setIcon(custom_icon_6989903e3d94433bae8efee3fc12c02c);
        
    
            var marker_b997d5f5d38140b1af70678d77da0d0a = L.marker(
                [-15.7118112, 39.3387113],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_9e8747a386bf49478ab00b3f0197dc43 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_b997d5f5d38140b1af70678d77da0d0a.setIcon(custom_icon_9e8747a386bf49478ab00b3f0197dc43);
        
    
            var marker_9518f34c46524dfd915cd64c52033c41 = L.marker(
                [-25.9555176, 32.5870339],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_8a688e9c6b544c62a3ca79c5ecdb01f5 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_9518f34c46524dfd915cd64c52033c41.setIcon(custom_icon_8a688e9c6b544c62a3ca79c5ecdb01f5);
        
    
            var marker_20e80ed8de2b43218b699769c0a00f47 = L.marker(
                [-25.9692673, 32.580017],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_748c227a7fe54723a1e5e6f82205b388 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_20e80ed8de2b43218b699769c0a00f47.setIcon(custom_icon_748c227a7fe54723a1e5e6f82205b388);
        
    
            var marker_0f1fe8f8ee7a43c0bcc6409f84fb2aef = L.marker(
                [-25.9719143, 32.5718009],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_3030795a24984b86b7ed04aa56c02e20 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_0f1fe8f8ee7a43c0bcc6409f84fb2aef.setIcon(custom_icon_3030795a24984b86b7ed04aa56c02e20);
        
    
            var marker_b05580b511a84d9a9f7abc9c8be20c69 = L.marker(
                [-25.9745774, 32.5846044],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_4bef41881f6b41f5b5a094c24c90ee70 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_b05580b511a84d9a9f7abc9c8be20c69.setIcon(custom_icon_4bef41881f6b41f5b5a094c24c90ee70);
        
    
            var marker_c30f47f3c95c42ed968bc476ebe6444b = L.marker(
                [-15.1219764, 39.2572608],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_2241d70041c04fc9b24934ad9ae3b4e5 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_c30f47f3c95c42ed968bc476ebe6444b.setIcon(custom_icon_2241d70041c04fc9b24934ad9ae3b4e5);
        
    
            var marker_173cf4741aa44ae1b2e61472398a444e = L.marker(
                [-15.126465, 39.2640253],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_aa4f29ced75941f19b5d4e8ffd392540 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_173cf4741aa44ae1b2e61472398a444e.setIcon(custom_icon_aa4f29ced75941f19b5d4e8ffd392540);
        
    
            var marker_844cd52da6ce4705a4cbe4e778dc0b04 = L.marker(
                [-15.1263769, 39.2642265],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_1eb97f0d6d594e96aa639f485cb5ec75 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_844cd52da6ce4705a4cbe4e778dc0b04.setIcon(custom_icon_1eb97f0d6d594e96aa639f485cb5ec75);
        
    
            var marker_70782eb0f70745a0bb8956e66d6b1814 = L.marker(
                [-15.1302569, 39.2683571],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_15e4df136b49433da885fa6bbe1f6541 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_70782eb0f70745a0bb8956e66d6b1814.setIcon(custom_icon_15e4df136b49433da885fa6bbe1f6541);
        
    
            var marker_53e76a78c30e4295818f01c63a703e51 = L.marker(
                [-15.1313071, 39.2683044],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_07648c74f8c24046ac152e6ad658ecbf = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_53e76a78c30e4295818f01c63a703e51.setIcon(custom_icon_07648c74f8c24046ac152e6ad658ecbf);
        
    
            var marker_91a1931a264a47f494ab31d6d184b972 = L.marker(
                [-15.1194603, 39.188781],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_642c5ba1c581418f8d8dc949ad006c47 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_91a1931a264a47f494ab31d6d184b972.setIcon(custom_icon_642c5ba1c581418f8d8dc949ad006c47);
        
    
            var marker_ba73c392c50e42aa8e33eebe20181ffd = L.marker(
                [-15.1114817, 39.2535337],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_92dd8a4845ee412aa1293419d331f644 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_ba73c392c50e42aa8e33eebe20181ffd.setIcon(custom_icon_92dd8a4845ee412aa1293419d331f644);
        
    
            var marker_5e25a6ef0ba441498ad7bedb6e15e440 = L.marker(
                [-15.1228572, 39.2581746],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_90b935bf521d4cabaaf8d920ec136376 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_5e25a6ef0ba441498ad7bedb6e15e440.setIcon(custom_icon_90b935bf521d4cabaaf8d920ec136376);
        
    
            var marker_e385b39492564876859a53364de8eb27 = L.marker(
                [-15.1088511, 39.2266121],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_58ffaf49d757487796b7c9d27e11c764 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_e385b39492564876859a53364de8eb27.setIcon(custom_icon_58ffaf49d757487796b7c9d27e11c764);
        
    
            var marker_95e338d81b44421b9594343ae7c66569 = L.marker(
                [-15.1368782, 39.2814854],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_aa4a5d6a248646c6b118f6734a6e500b = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_95e338d81b44421b9594343ae7c66569.setIcon(custom_icon_aa4a5d6a248646c6b118f6734a6e500b);
        
    
            var marker_13dfb4c207f7438ab87c693691f31fa8 = L.marker(
                [-15.0325491, 40.7358993],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_f60a3d6cb39d4d4e95d0e0a022ee0e20 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_13dfb4c207f7438ab87c693691f31fa8.setIcon(custom_icon_f60a3d6cb39d4d4e95d0e0a022ee0e20);
        
    
            var marker_c50d6394b4344e7b92b5c60d8964c335 = L.marker(
                [-15.194591, 35.8703362],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_1b0ea704c8034ae2a9424420e68f8388 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_c50d6394b4344e7b92b5c60d8964c335.setIcon(custom_icon_1b0ea704c8034ae2a9424420e68f8388);
        
    
            var marker_e25a01ebd8b7447da536abb16fa83333 = L.marker(
                [-25.4043655, 32.8061388],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_4e5abbd894974c0a93807ffac59b146c = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_e25a01ebd8b7447da536abb16fa83333.setIcon(custom_icon_4e5abbd894974c0a93807ffac59b146c);
        
    
            var marker_155302ced2304cbcb0784ecaafce1db8 = L.marker(
                [-25.4055757, 32.8047011],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ebedbaef3e844a808b69b81e773ecf80 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_155302ced2304cbcb0784ecaafce1db8.setIcon(custom_icon_ebedbaef3e844a808b69b81e773ecf80);
        
    
            var marker_835d8e1824bc4ddfbfeaff54f0494110 = L.marker(
                [-17.9797289, 35.7121196],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_58b46b49b97d46c989e86db9758d054a = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_835d8e1824bc4ddfbfeaff54f0494110.setIcon(custom_icon_58b46b49b97d46c989e86db9758d054a);
        
    
            var marker_7e158342793046008fe6c86b16644bad = L.marker(
                [-17.9802059, 35.7115469],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_225614992dac48f8ac38fc9d1a3e36f5 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_7e158342793046008fe6c86b16644bad.setIcon(custom_icon_225614992dac48f8ac38fc9d1a3e36f5);
        
    
            var marker_c3d52f823a244ca088ff4c492cfb9fe8 = L.marker(
                [-17.9795957, 35.7123812],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_0fdca198c661427ab23f5f9a4856745e = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_c3d52f823a244ca088ff4c492cfb9fe8.setIcon(custom_icon_0fdca198c661427ab23f5f9a4856745e);
        
    
            var marker_b6c9d5f2b99041ffb6846130b03cd01a = L.marker(
                [-17.9797334, 35.7128855],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_4a2afe22f250470c95f0bdefe06076fc = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_b6c9d5f2b99041ffb6846130b03cd01a.setIcon(custom_icon_4a2afe22f250470c95f0bdefe06076fc);
        
    
            var marker_80c9f9f8b67543659cdd2dcd6968efbe = L.marker(
                [-23.845039, 35.5025569],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_cf2a46fa4ec4456fbe5dce3b2d8028b7 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_80c9f9f8b67543659cdd2dcd6968efbe.setIcon(custom_icon_cf2a46fa4ec4456fbe5dce3b2d8028b7);
        
    
            var marker_8127a25e6aa24c15b5be23f33c788876 = L.marker(
                [-16.8324689, 36.9636505],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_360263cda7f441afa5b1220b857f74ed = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_8127a25e6aa24c15b5be23f33c788876.setIcon(custom_icon_360263cda7f441afa5b1220b857f74ed);
        
    
            var marker_3bafa5aa42ea488689569b55fbc3395e = L.marker(
                [-16.8326727, 36.9632978],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_3ef11468dc2346c380ecdf3a5c26e384 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_3bafa5aa42ea488689569b55fbc3395e.setIcon(custom_icon_3ef11468dc2346c380ecdf3a5c26e384);
        
    
            var marker_213e059560c440bf91cfc8b2fe97ff91 = L.marker(
                [-23.8447169, 35.5020096],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_62f85c60ace34e2fb237fdc58c1bc6a0 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_213e059560c440bf91cfc8b2fe97ff91.setIcon(custom_icon_62f85c60ace34e2fb237fdc58c1bc6a0);
        
    
            var marker_3e1ee92b71e74674be279e9f19696a44 = L.marker(
                [-25.9647801, 32.5981646],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_2413fa528134497fb92000b2708d3700 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_3e1ee92b71e74674be279e9f19696a44.setIcon(custom_icon_2413fa528134497fb92000b2708d3700);
        
    
            var marker_6a11bf9c5eb842d89f848ee574ee3978 = L.marker(
                [-25.9632373, 32.5761476],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ba59ad2daec44876834c08ecbb3abbba = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_6a11bf9c5eb842d89f848ee574ee3978.setIcon(custom_icon_ba59ad2daec44876834c08ecbb3abbba);
        
    
            var marker_8eeeca6551e343a895cdbb7fdb670573 = L.marker(
                [-25.9551557, 32.5927475],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_aaf9f00444164d1fafdb7655d94d14ca = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_8eeeca6551e343a895cdbb7fdb670573.setIcon(custom_icon_aaf9f00444164d1fafdb7655d94d14ca);
        
    
            var marker_02deb0ed32934adcbb6d6ac6121e5a40 = L.marker(
                [-25.7706117, 32.565407],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_5cc3424f0a83457895040e82c12ce8c4 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_02deb0ed32934adcbb6d6ac6121e5a40.setIcon(custom_icon_5cc3424f0a83457895040e82c12ce8c4);
        
    
            var marker_dbe3375da878471bb6d3e9adcee3cf36 = L.marker(
                [-25.9770681, 32.5928092],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_59212462d1ab4120ad9691ec88ae6a44 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_dbe3375da878471bb6d3e9adcee3cf36.setIcon(custom_icon_59212462d1ab4120ad9691ec88ae6a44);
        
    
            var marker_4c7e92c5fd944731a1c7b659ae0d4106 = L.marker(
                [-25.9748751, 32.5900615],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_927fbf284d8e471a83e7f508badef6da = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_4c7e92c5fd944731a1c7b659ae0d4106.setIcon(custom_icon_927fbf284d8e471a83e7f508badef6da);
        
    
            var marker_61205920000d42f2b2100f9f2723db93 = L.marker(
                [-25.9759129, 32.576629],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_70b6793e7f5c4c7b8a84fb3bcee6f53e = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_61205920000d42f2b2100f9f2723db93.setIcon(custom_icon_70b6793e7f5c4c7b8a84fb3bcee6f53e);
        
    
            var marker_268b466861fb44ebb5ca2d8d1b5765af = L.marker(
                [-12.9684795, 40.5333848],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_eef28069763e441a82f93017217b2bd4 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_268b466861fb44ebb5ca2d8d1b5765af.setIcon(custom_icon_eef28069763e441a82f93017217b2bd4);
        
    
            var marker_b9bf74a6c92a4856a265fff562d759c1 = L.marker(
                [-14.9572662, 37.4065935],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_e3ee804341ca427cacf1d02aa14ee234 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_b9bf74a6c92a4856a265fff562d759c1.setIcon(custom_icon_e3ee804341ca427cacf1d02aa14ee234);
        
    
            var marker_5a1f76c0d6b9408093f8ae3b4f16ff1d = L.marker(
                [-25.9708504, 32.5702481],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_78de40fe9fed4bcb82221956c87140e9 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_5a1f76c0d6b9408093f8ae3b4f16ff1d.setIcon(custom_icon_78de40fe9fed4bcb82221956c87140e9);
        
    
            var marker_23bbbf9f3de747749391c3428cbe2eac = L.marker(
                [-25.9706316, 32.5704286],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_042c2508864b48a2925e05f3935fbc63 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_23bbbf9f3de747749391c3428cbe2eac.setIcon(custom_icon_042c2508864b48a2925e05f3935fbc63);
        
    
            var marker_69a9d8647b2f4ab796f479ffb08dbe37 = L.marker(
                [-25.9679538, 32.5721288],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_dd541467576c47d7905ed072b1f7e818 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_69a9d8647b2f4ab796f479ffb08dbe37.setIcon(custom_icon_dd541467576c47d7905ed072b1f7e818);
        
    
            var marker_c2c88738159b4e3b883f3435962ad966 = L.marker(
                [-25.9725106, 32.5689844],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_b080e114bbe24438ac62db24fac0d8c3 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_c2c88738159b4e3b883f3435962ad966.setIcon(custom_icon_b080e114bbe24438ac62db24fac0d8c3);
        
    
            var marker_52842ed9f6eb40f2948e3ea816a77186 = L.marker(
                [-25.9646452, 32.5699819],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_9394e9e8be3148bd9b5afb9fa18c73cc = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_52842ed9f6eb40f2948e3ea816a77186.setIcon(custom_icon_9394e9e8be3148bd9b5afb9fa18c73cc);
        
    
            var marker_a3b8165d49fe475383584c1ef493006b = L.marker(
                [-14.3971991, 34.3437566],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_8cd11d5cdae6491a978c20233290599f = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_a3b8165d49fe475383584c1ef493006b.setIcon(custom_icon_8cd11d5cdae6491a978c20233290599f);
        
    
            var marker_3f637dc501dd46638eee13fc9c028600 = L.marker(
                [-14.3948107, 34.3357839],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_567f5168ed9145dc9fa50c2de0369bb5 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_3f637dc501dd46638eee13fc9c028600.setIcon(custom_icon_567f5168ed9145dc9fa50c2de0369bb5);
        
    
            var marker_083a6c1824e9444ab3503edefed3fdb7 = L.marker(
                [-15.043418, 40.6950769],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_792238e020174e31bc97b5c9ee7a8e15 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_083a6c1824e9444ab3503edefed3fdb7.setIcon(custom_icon_792238e020174e31bc97b5c9ee7a8e15);
        
    
            var marker_115975b8b495440785f70474a175780a = L.marker(
                [-15.1192374, 39.2684607],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_68278c9c3460414395f5159c97388b3a = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_115975b8b495440785f70474a175780a.setIcon(custom_icon_68278c9c3460414395f5159c97388b3a);
        
    
            var marker_2ed4fb5e71e74acbac1849b8e2eced87 = L.marker(
                [-15.1162613, 39.2648342],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_be75d8abe5c44386b13686c793401952 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_2ed4fb5e71e74acbac1849b8e2eced87.setIcon(custom_icon_be75d8abe5c44386b13686c793401952);
        
    
            var marker_339bae9d7a5540a0ad103ba58a57e6fd = L.marker(
                [-15.1164693, 39.2663303],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_2f93010e2f55446cbf8d821547c6ae28 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_339bae9d7a5540a0ad103ba58a57e6fd.setIcon(custom_icon_2f93010e2f55446cbf8d821547c6ae28);
        
    
            var marker_6ff635df2d3e45758d9370115f21ce3d = L.marker(
                [-15.1178738, 39.2654249],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_45c0b6b5349f4f47b9c32e7ecb2e037e = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_6ff635df2d3e45758d9370115f21ce3d.setIcon(custom_icon_45c0b6b5349f4f47b9c32e7ecb2e037e);
        
    
            var marker_4166f23becf5450f946e7b6719954480 = L.marker(
                [-15.123526, 39.258013],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_aff97c83fd2049fa846f8c0f632b327e = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_4166f23becf5450f946e7b6719954480.setIcon(custom_icon_aff97c83fd2049fa846f8c0f632b327e);
        
    
            var marker_52766a91c6bc41628fc1e9bddf93d844 = L.marker(
                [-15.1196692, 39.2645918],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_1b7ebb9b0a484a329bbbd1c21865e488 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_52766a91c6bc41628fc1e9bddf93d844.setIcon(custom_icon_1b7ebb9b0a484a329bbbd1c21865e488);
        
    
            var marker_7337ba2e12bf44bfa5cbc49dd9a8a4b4 = L.marker(
                [-26.8422927, 32.8865886],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_9ec9ca494ba0448db7dbe7279ce040ae = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_7337ba2e12bf44bfa5cbc49dd9a8a4b4.setIcon(custom_icon_9ec9ca494ba0448db7dbe7279ce040ae);
        
    
            var marker_70c0adca722d45de8a9b522ca97ff89c = L.marker(
                [-26.8422692, 32.8865987],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ca4e9d35913e493c833bd9bc1ae1629d = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_70c0adca722d45de8a9b522ca97ff89c.setIcon(custom_icon_ca4e9d35913e493c833bd9bc1ae1629d);
        
    
            var marker_b1fdcb7b9f89466c9aa52b758e06fec5 = L.marker(
                [-24.7109971, 33.8853036],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_b431e08d7e8e426e89591c7cf244ea4f = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_b1fdcb7b9f89466c9aa52b758e06fec5.setIcon(custom_icon_b431e08d7e8e426e89591c7cf244ea4f);
        
    
            var marker_3489d2f69a7742a29dc720424fe34aa6 = L.marker(
                [-25.8883386, 32.5650714],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_bd72771675c747abb66984c3b1fa4f72 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_3489d2f69a7742a29dc720424fe34aa6.setIcon(custom_icon_bd72771675c747abb66984c3b1fa4f72);
        
    
            var marker_dcf2555e9cca403ba8f656ad80463e24 = L.marker(
                [-14.9152716, 36.3660922],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_10d39ebe4294416b8aefcc3b4cb68c9a = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_dcf2555e9cca403ba8f656ad80463e24.setIcon(custom_icon_10d39ebe4294416b8aefcc3b4cb68c9a);
        
    
            var marker_6d92f922c2a44d1bab16d9d50d800e84 = L.marker(
                [-14.9152701, 36.3663027],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_4f70cd7ba4e04535b91a0f8aadbf9431 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_6d92f922c2a44d1bab16d9d50d800e84.setIcon(custom_icon_4f70cd7ba4e04535b91a0f8aadbf9431);
        
    
            var marker_d885e20dbbc84da393a7c02c6d6b4d15 = L.marker(
                [-25.8540585, 32.5443122],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_f741852641c34161801f02b991d7dfcf = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_d885e20dbbc84da393a7c02c6d6b4d15.setIcon(custom_icon_f741852641c34161801f02b991d7dfcf);
        
    
            var marker_35838850a62048a6b7079e465b7b641b = L.marker(
                [-16.2341213, 39.9073425],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_5ce7cebe11f74198b27036b49a1049df = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_35838850a62048a6b7079e465b7b641b.setIcon(custom_icon_5ce7cebe11f74198b27036b49a1049df);
        
    
            var marker_cf2bb9aa88014edaab5ca2711cdab627 = L.marker(
                [-25.9737544, 32.5878458],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_6df0b941dab44a56b133a88a36cc061e = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_cf2bb9aa88014edaab5ca2711cdab627.setIcon(custom_icon_6df0b941dab44a56b133a88a36cc061e);
        
    
            var marker_c1467391f24e499a8374b0d72cbbea34 = L.marker(
                [-25.9159051, 32.5897183],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_16cd03812dd845059095ec74ef260df6 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_c1467391f24e499a8374b0d72cbbea34.setIcon(custom_icon_16cd03812dd845059095ec74ef260df6);
        
    
            var marker_2f1340d8345d41c6ae3a185ddcf3cd13 = L.marker(
                [-25.9126146, 32.5901397],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_830a09083e334e0aa9f5a8ba482511e2 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_2f1340d8345d41c6ae3a185ddcf3cd13.setIcon(custom_icon_830a09083e334e0aa9f5a8ba482511e2);
        
    
            var marker_b89bf271fdc44b0e9e2d512ff741f68e = L.marker(
                [-25.9639487, 32.5867503],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_200d953cbf114f818144317eb9a4fffe = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_b89bf271fdc44b0e9e2d512ff741f68e.setIcon(custom_icon_200d953cbf114f818144317eb9a4fffe);
        
    
            var marker_1af648167c7c48159ffa5fe28735143d = L.marker(
                [-13.1966663, 37.4986293],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_3b4f12e648e34a618698a2c0037e2842 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_1af648167c7c48159ffa5fe28735143d.setIcon(custom_icon_3b4f12e648e34a618698a2c0037e2842);
        
    
            var marker_7796c220c2b54d8ea88dedaa34b4bfb6 = L.marker(
                [-13.1977944, 37.4988062],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_e9b8d8bc0df541b8bd2bf8b86dc2f801 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_7796c220c2b54d8ea88dedaa34b4bfb6.setIcon(custom_icon_e9b8d8bc0df541b8bd2bf8b86dc2f801);
        
    
            var marker_9442f882a80344499c4ac9fc0334d5c3 = L.marker(
                [-22.8555637, 35.1806182],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_bb4b0c82de2d4388875ace1ec66b2f58 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_9442f882a80344499c4ac9fc0334d5c3.setIcon(custom_icon_bb4b0c82de2d4388875ace1ec66b2f58);
        
    
            var marker_3662275fbc2340c2985a4a626ea6f31e = L.marker(
                [-21.9903677, 35.3189325],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_cd45bfcd93584deda03a4d2db5dc6e64 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_3662275fbc2340c2985a4a626ea6f31e.setIcon(custom_icon_cd45bfcd93584deda03a4d2db5dc6e64);
        
    
            var marker_7d91b6d9e6254e7cbbe185909edeac9e = L.marker(
                [-25.9375081, 32.5998615],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_7ff487f747664ba3aae851b55775317f = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_7d91b6d9e6254e7cbbe185909edeac9e.setIcon(custom_icon_7ff487f747664ba3aae851b55775317f);
        
    
            var marker_8646b7b233d74a21b202a2ea9bee8119 = L.marker(
                [-19.1240443, 33.4807053],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_36a76f8a6e964d569e029335f82baf5a = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_8646b7b233d74a21b202a2ea9bee8119.setIcon(custom_icon_36a76f8a6e964d569e029335f82baf5a);
        
    
            var marker_e84c09f23edc425ea0c3a620e0cb0ab4 = L.marker(
                [-16.9732285, 33.3211967],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_e4b218e314c848ea9d7c3df7fbe2fe07 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_e84c09f23edc425ea0c3a620e0cb0ab4.setIcon(custom_icon_e4b218e314c848ea9d7c3df7fbe2fe07);
        
    
            var marker_660c92ddc2dc42799bc7a8ca7fca158f = L.marker(
                [-12.9635241, 40.5006054],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_5ea6aeeb325345928fe2425de2df5791 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_660c92ddc2dc42799bc7a8ca7fca158f.setIcon(custom_icon_5ea6aeeb325345928fe2425de2df5791);
        
    
            var marker_47888364a01f48d5909bee5fa3bc63a9 = L.marker(
                [-25.9312616, 32.5716732],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_86df9481b0de48fcbd8312bcb0fa6cc1 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_47888364a01f48d5909bee5fa3bc63a9.setIcon(custom_icon_86df9481b0de48fcbd8312bcb0fa6cc1);
        
    
            var marker_0ccd86163f5f42a8a707d6f949b032cd = L.marker(
                [-20.6997475, 32.4772074],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a4cd1dc76bb343338d0428adcf2dc940 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_0ccd86163f5f42a8a707d6f949b032cd.setIcon(custom_icon_a4cd1dc76bb343338d0428adcf2dc940);
        
    
            var marker_2194fec0f62a42daa2c2a82d18af7988 = L.marker(
                [-19.7248894, 34.8194789],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_80aacf411c624e979d870481587fb915 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_2194fec0f62a42daa2c2a82d18af7988.setIcon(custom_icon_80aacf411c624e979d870481587fb915);
        
    
            var marker_8ff684d09e6b49d5a808789f0b82ee61 = L.marker(
                [-19.7461948, 34.8472248],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_b0fc09ce1a704e538e5ee94979388031 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_8ff684d09e6b49d5a808789f0b82ee61.setIcon(custom_icon_b0fc09ce1a704e538e5ee94979388031);
        
    
            var marker_fde8ceafa53849c9b42e1080358570d9 = L.marker(
                [-11.0755723, 39.2572579],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_54179b475380487fbe07c102a2fc59d8 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_fde8ceafa53849c9b42e1080358570d9.setIcon(custom_icon_54179b475380487fbe07c102a2fc59d8);
        
    
            var marker_43c80368c22b45fb90d341c3686aad4b = L.marker(
                [-26.0201283, 32.4005174],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_8176a4ea83cf4b80b9d7801d381d537a = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_43c80368c22b45fb90d341c3686aad4b.setIcon(custom_icon_8176a4ea83cf4b80b9d7801d381d537a);
        
    
            var marker_47f32acaec6447e0bec79e8f2f358754 = L.marker(
                [-12.6948145, 34.8083867],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_1862f91925de40019a663015969d256a = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_47f32acaec6447e0bec79e8f2f358754.setIcon(custom_icon_1862f91925de40019a663015969d256a);
        
    
            var marker_88fdf3cc558a46e39af2cb1e626794da = L.marker(
                [-25.95612, 32.570893],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_96028994445e42718b9a5463e38ce7cd = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_88fdf3cc558a46e39af2cb1e626794da.setIcon(custom_icon_96028994445e42718b9a5463e38ce7cd);
        
    
            var marker_2cd075d703fc4444bcb8c8be80408305 = L.marker(
                [-25.9146734, 32.6133627],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_0fe648aef9c5401f9d8d807b825790a8 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_2cd075d703fc4444bcb8c8be80408305.setIcon(custom_icon_0fe648aef9c5401f9d8d807b825790a8);
        
    
            var marker_eb39ac0fdd454179bde693917d700b04 = L.marker(
                [-25.9162794, 32.610061],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_9c0a82d578114cc8a99e2c0bd7c6cc6f = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_eb39ac0fdd454179bde693917d700b04.setIcon(custom_icon_9c0a82d578114cc8a99e2c0bd7c6cc6f);
        
    
            var marker_bdd76a6ef4da49a387f0d0d5792b4b14 = L.marker(
                [-15.7395934, 32.7689368],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_619f32c84a2e4b069f97330d20978efb = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_bdd76a6ef4da49a387f0d0d5792b4b14.setIcon(custom_icon_619f32c84a2e4b069f97330d20978efb);
        
    
            var marker_1db0d3b48b194ac78456b8d20d2a4b7c = L.marker(
                [-25.9151483, 32.6099309],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_d97d49fd300c42a082f86f16aacc0e4d = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_1db0d3b48b194ac78456b8d20d2a4b7c.setIcon(custom_icon_d97d49fd300c42a082f86f16aacc0e4d);
        
    
            var marker_814457e1584847bb9da366aa189524a6 = L.marker(
                [-25.8965001, 32.5634657],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_52f090948cab4cad9e66603dd4e2cbd6 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_814457e1584847bb9da366aa189524a6.setIcon(custom_icon_52f090948cab4cad9e66603dd4e2cbd6);
        
    
            var marker_acdd17e720e944bdb0f86b7aaf6e95df = L.marker(
                [-25.8541915, 32.5677411],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_dd8c51182ab7475782cf3997a80fa2e4 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_acdd17e720e944bdb0f86b7aaf6e95df.setIcon(custom_icon_dd8c51182ab7475782cf3997a80fa2e4);
        
    
            var marker_edb0482716284ee19e29f9454a751bcd = L.marker(
                [-14.5465992, 40.6829251],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_10478f7e18d5405b9fd840ba293409be = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_edb0482716284ee19e29f9454a751bcd.setIcon(custom_icon_10478f7e18d5405b9fd840ba293409be);
        
    
            var marker_eeea574362d94833b9515c4c2d73d4ad = L.marker(
                [-14.5433655, 40.6794016],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_fa0f17b6c89041919e2ac98ce36dd650 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_eeea574362d94833b9515c4c2d73d4ad.setIcon(custom_icon_fa0f17b6c89041919e2ac98ce36dd650);
        
    
            var marker_729179bc862a48a4a16335e4a8a25164 = L.marker(
                [-25.9598912, 32.5689077],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_bb965a2537ca45b3900a93e176c273e4 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_729179bc862a48a4a16335e4a8a25164.setIcon(custom_icon_bb965a2537ca45b3900a93e176c273e4);
        
    
            var marker_67d6bb9c30fe44ccbf86416fab44e059 = L.marker(
                [-25.9652439, 32.5847307],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_7165b5d91f6e441eb8f8013b9c26c2ec = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_67d6bb9c30fe44ccbf86416fab44e059.setIcon(custom_icon_7165b5d91f6e441eb8f8013b9c26c2ec);
        
    
            var marker_bc9728ad435e4c88aa6dc09b808a4309 = L.marker(
                [-25.9589724, 32.5700758],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_e0fae780f2974482b152d59162b01599 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_bc9728ad435e4c88aa6dc09b808a4309.setIcon(custom_icon_e0fae780f2974482b152d59162b01599);
        
    
            var marker_5b6000f0ce804f1c9d21c5080e415c6c = L.marker(
                [-25.9721423, 32.5946703],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ffff93ab8e0f4f1e83879d8695fcf4f2 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_5b6000f0ce804f1c9d21c5080e415c6c.setIcon(custom_icon_ffff93ab8e0f4f1e83879d8695fcf4f2);
        
    
            var marker_06a180ab13ed4ebfb7e1cceb5cf73db9 = L.marker(
                [-21.9506719, 35.3134781],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_045c3f36bef04e15894fd67327452f18 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_06a180ab13ed4ebfb7e1cceb5cf73db9.setIcon(custom_icon_045c3f36bef04e15894fd67327452f18);
        
    
            var marker_9cd04353180e469cb8a25a679255a8fb = L.marker(
                [-23.8557143, 35.5475954],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_0877e8b8fdcb4eba846b76b643979e90 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_9cd04353180e469cb8a25a679255a8fb.setIcon(custom_icon_0877e8b8fdcb4eba846b76b643979e90);
        
    
            var marker_2ce29b4724a64c0d93a59082f520d7b3 = L.marker(
                [-12.9646766, 40.5044109],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_c2da3231bdf346ac8cc0243199683820 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_2ce29b4724a64c0d93a59082f520d7b3.setIcon(custom_icon_c2da3231bdf346ac8cc0243199683820);
        
    
            var marker_aece00569130413da8e9e218f50cee2e = L.marker(
                [-12.9677513, 40.5006307],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_f7b0889790b047c09cbe710b8adc6b75 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_aece00569130413da8e9e218f50cee2e.setIcon(custom_icon_f7b0889790b047c09cbe710b8adc6b75);
        
    
            var marker_d970ddbd5ce94de395f57da2c3f49dcf = L.marker(
                [-12.9877506, 40.5319309],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_7c6703170fe64db8a645af3c132e7265 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_d970ddbd5ce94de395f57da2c3f49dcf.setIcon(custom_icon_7c6703170fe64db8a645af3c132e7265);
        
    
            var marker_c62d3f6c74c642609a18811eeace7c61 = L.marker(
                [-12.9908274, 40.5286775],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_c7ad63671aa743afa42e8fcc85a99685 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_c62d3f6c74c642609a18811eeace7c61.setIcon(custom_icon_c7ad63671aa743afa42e8fcc85a99685);
        
    
            var marker_c659cdcc34dc4f68b8f4335a674525df = L.marker(
                [-12.9803535, 40.5415393],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ba42279b65f3413e9d5c1d27b8238681 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_c659cdcc34dc4f68b8f4335a674525df.setIcon(custom_icon_ba42279b65f3413e9d5c1d27b8238681);
        
    
            var marker_6265e89b25f04157b9315b8d1f940eae = L.marker(
                [-25.9353166, 32.5565511],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_db4d853fb04d46e48227a6ff630183d7 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_6265e89b25f04157b9315b8d1f940eae.setIcon(custom_icon_db4d853fb04d46e48227a6ff630183d7);
        
    
            var marker_388e9d6fdd2b4d8f84e466ba432763d5 = L.marker(
                [-25.9341412, 32.5497872],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ec7fbed8d028441fb77273d1f367e869 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_388e9d6fdd2b4d8f84e466ba432763d5.setIcon(custom_icon_ec7fbed8d028441fb77273d1f367e869);
        
    
            var marker_6ce9374dbbba420ba3d08943effeb711 = L.marker(
                [-25.9253704, 32.6083247],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_5ea727b489eb451e838378029a6a10d6 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_6ce9374dbbba420ba3d08943effeb711.setIcon(custom_icon_5ea727b489eb451e838378029a6a10d6);
        
    
            var marker_c3d8f8b527364bf09ad16a7b6c69cd40 = L.marker(
                [-25.929594, 32.6333731],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a75cb6c483484658b119c4feeff013ff = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_c3d8f8b527364bf09ad16a7b6c69cd40.setIcon(custom_icon_a75cb6c483484658b119c4feeff013ff);
        
    
            var marker_c598233b81ca4c19bbb2d08ff1db1575 = L.marker(
                [-22.0000796, 35.318793],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_43ca9d50561a45dea381250bb202f102 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_c598233b81ca4c19bbb2d08ff1db1575.setIcon(custom_icon_43ca9d50561a45dea381250bb202f102);
        
    
            var marker_5ccf549d34ef4c2d82362a9e2decd8e7 = L.marker(
                [-17.8706763, 36.8876081],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a7725bba92354f6daef2c68005d44879 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_5ccf549d34ef4c2d82362a9e2decd8e7.setIcon(custom_icon_a7725bba92354f6daef2c68005d44879);
        
    
            var marker_612aec65d4644f259cb1c43bbe50a2c9 = L.marker(
                [-17.8784024, 36.8863141],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_5aa85e887df7498499d135780c981af4 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_612aec65d4644f259cb1c43bbe50a2c9.setIcon(custom_icon_5aa85e887df7498499d135780c981af4);
        
    
            var marker_ff8f2394c7424ca3ad84c75d23a9aa39 = L.marker(
                [-17.8754562, 36.8819783],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_eb28d9dbf0894e9ab0e34fd8b66bd6b9 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_ff8f2394c7424ca3ad84c75d23a9aa39.setIcon(custom_icon_eb28d9dbf0894e9ab0e34fd8b66bd6b9);
        
    
            var marker_24061f6efabd4dde8e1108e1bb9ecd17 = L.marker(
                [-16.2186898, 39.8990654],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_f120208c925c4b00953399f947dc11e3 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_24061f6efabd4dde8e1108e1bb9ecd17.setIcon(custom_icon_f120208c925c4b00953399f947dc11e3);
        
    
            var marker_e8871918fbf34dd0ab924a6ef2d11a03 = L.marker(
                [-24.0434561, 35.0884598],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_037dec51ff824f0098a81ef89fc86b98 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_e8871918fbf34dd0ab924a6ef2d11a03.setIcon(custom_icon_037dec51ff824f0098a81ef89fc86b98);
        
    
            var marker_765aa18bb1ff4f81a205267df2c9c8d8 = L.marker(
                [-23.6593025, 35.1614669],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_cbefed0b3d134899842ece682ab86d26 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_765aa18bb1ff4f81a205267df2c9c8d8.setIcon(custom_icon_cbefed0b3d134899842ece682ab86d26);
        
    
            var marker_0bc77153ca2a473fb292257f1c4419b8 = L.marker(
                [-23.7394224, 34.9767673],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_dac4c9494f2b46a7bcbce5da258a82c3 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_0bc77153ca2a473fb292257f1c4419b8.setIcon(custom_icon_dac4c9494f2b46a7bcbce5da258a82c3);
        
    
            var marker_39f87773e7c743fbbeb39c0b05339d87 = L.marker(
                [-23.5537715, 35.3404185],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_5ca1cf6791324f4bb30cd45b8c61f0a5 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_39f87773e7c743fbbeb39c0b05339d87.setIcon(custom_icon_5ca1cf6791324f4bb30cd45b8c61f0a5);
        
    
            var marker_46669733f5ec4b5a8f69a66c81efa8ad = L.marker(
                [-11.5466927, 35.0604542],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_f12c9b15dd514a5db993eaf31fbc76f3 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_46669733f5ec4b5a8f69a66c81efa8ad.setIcon(custom_icon_f12c9b15dd514a5db993eaf31fbc76f3);
        
    
            var marker_505fae5aa3664e8b9a2a8581f6d817b1 = L.marker(
                [-19.8314851, 34.8664597],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_44cff56fe050449982609ce534933356 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_505fae5aa3664e8b9a2a8581f6d817b1.setIcon(custom_icon_44cff56fe050449982609ce534933356);
        
    
            var marker_f1edf922339643b28b6ce9d04b9335f1 = L.marker(
                [-19.8490298, 34.8752098],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_14c2b04d1e2646e6ae31c2eae926e55e = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_f1edf922339643b28b6ce9d04b9335f1.setIcon(custom_icon_14c2b04d1e2646e6ae31c2eae926e55e);
        
    
            var marker_44b3110a97534207b38af2bf05ec9e6f = L.marker(
                [-19.7469002, 34.8605631],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_31d314e67fdf43bb950e93b451a2baa9 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_44b3110a97534207b38af2bf05ec9e6f.setIcon(custom_icon_31d314e67fdf43bb950e93b451a2baa9);
        
    
            var marker_e7285b118353431c96a9ed1a670bf144 = L.marker(
                [-19.8017717, 34.8908967],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_de1eb111b8f14f58a46636893dc46724 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_e7285b118353431c96a9ed1a670bf144.setIcon(custom_icon_de1eb111b8f14f58a46636893dc46724);
        
    
            var marker_58edf42487a747628105fe7239f2ccbd = L.marker(
                [-25.961966, 32.5771319],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_2b8eed1a0e484212aee9c36d898b01e6 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_58edf42487a747628105fe7239f2ccbd.setIcon(custom_icon_2b8eed1a0e484212aee9c36d898b01e6);
        
    
            var marker_1ce5d169943f47eba67c17ef14a10be5 = L.marker(
                [-19.8829819, 34.5927733],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_b76041155c1e418091e0c4e1b3d9423a = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_1ce5d169943f47eba67c17ef14a10be5.setIcon(custom_icon_b76041155c1e418091e0c4e1b3d9423a);
        
    
            var marker_c7cb24cfbff24034bdf5232bd1f8e1f1 = L.marker(
                [-19.3639757, 34.5748517],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_c19d3354cd774173839308e2c4e521e5 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_c7cb24cfbff24034bdf5232bd1f8e1f1.setIcon(custom_icon_c19d3354cd774173839308e2c4e521e5);
        
    
            var marker_133b414b8390408689e74370327c54cc = L.marker(
                [-19.5030938, 34.5933026],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_9602594bffc7423c99dc8fb4230e9387 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_133b414b8390408689e74370327c54cc.setIcon(custom_icon_9602594bffc7423c99dc8fb4230e9387);
        
    
            var marker_73642afaeef44c7bb8af5ceecbdbfef7 = L.marker(
                [-19.5435948, 34.6258056],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_7453b1746c984a2fb8a21f4c460f66db = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_73642afaeef44c7bb8af5ceecbdbfef7.setIcon(custom_icon_7453b1746c984a2fb8a21f4c460f66db);
        
    
            var marker_d8002ee8641d483887165ee5b0710cc7 = L.marker(
                [-19.6297038, 34.7173762],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_dbf342d451d34a63af6f423eabc6bb02 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_d8002ee8641d483887165ee5b0710cc7.setIcon(custom_icon_dbf342d451d34a63af6f423eabc6bb02);
        
    
            var marker_6b9bde2c58314f099463c8c44804a2c7 = L.marker(
                [-19.6181757, 34.7412184],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_564eda7f561d42dd87abab322e032198 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_6b9bde2c58314f099463c8c44804a2c7.setIcon(custom_icon_564eda7f561d42dd87abab322e032198);
        
    
            var marker_97d34477d75d4b9d91f6a43612a2d32b = L.marker(
                [-19.6871573, 34.7600126],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_71431f4e411c4fc6a77f335a2228b09f = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_97d34477d75d4b9d91f6a43612a2d32b.setIcon(custom_icon_71431f4e411c4fc6a77f335a2228b09f);
        
    
            var marker_b028b62b032f4c4eb6b707b1c93eae3d = L.marker(
                [-12.2461005, 40.1255934],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_e542f9dc818748ef8dc9f0da0f900102 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_b028b62b032f4c4eb6b707b1c93eae3d.setIcon(custom_icon_e542f9dc818748ef8dc9f0da0f900102);
        
    
            var marker_1cbfbcf3689a42fda26c7897d8cc5c7c = L.marker(
                [-12.0683107, 40.4777822],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_2177f149e2134c4f94801545942ecd1b = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_1cbfbcf3689a42fda26c7897d8cc5c7c.setIcon(custom_icon_2177f149e2134c4f94801545942ecd1b);
        
    
            var marker_d3b60c6b161f41e4a0023afed834396f = L.marker(
                [-12.4320111, 40.4832968],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_5c03625ca730490390e4ea9514b6b726 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_d3b60c6b161f41e4a0023afed834396f.setIcon(custom_icon_5c03625ca730490390e4ea9514b6b726);
        
    
            var marker_44f425928f054046a654df3e0049c96d = L.marker(
                [-12.3435719, 40.5847594],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_6fb87a3179464b2d9705c034c6ad655f = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_44f425928f054046a654df3e0049c96d.setIcon(custom_icon_6fb87a3179464b2d9705c034c6ad655f);
        
    
            var marker_00f41197af7f4767b67e5cfb877a37f9 = L.marker(
                [-12.435982, 40.4968621],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_89baa09cda98426aad9c40860021b7af = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_00f41197af7f4767b67e5cfb877a37f9.setIcon(custom_icon_89baa09cda98426aad9c40860021b7af);
        
    
            var marker_d92cffc58db44c08bc737829483cc922 = L.marker(
                [-12.3442571, 40.3139824],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a2c1e90de1d345b28d4e159256f35224 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_d92cffc58db44c08bc737829483cc922.setIcon(custom_icon_a2c1e90de1d345b28d4e159256f35224);
        
    
            var marker_0396a4da3fd74f4d806330ae1c6f7940 = L.marker(
                [-12.3800216, 40.2642663],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_2dbd8a26048f4dad81dc1f2a051810a6 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_0396a4da3fd74f4d806330ae1c6f7940.setIcon(custom_icon_2dbd8a26048f4dad81dc1f2a051810a6);
        
    
            var marker_2631683f4e2b4639ae5646b86842f4d6 = L.marker(
                [-12.3963991, 40.107463],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_6e5d3a9dc02e4bce950940850acedc1c = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_2631683f4e2b4639ae5646b86842f4d6.setIcon(custom_icon_6e5d3a9dc02e4bce950940850acedc1c);
        
    
            var marker_41f96256541e476f989a80c5faf9b92d = L.marker(
                [-11.9311123, 40.1073933],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_45595205f9714201907adb1154e0da41 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_41f96256541e476f989a80c5faf9b92d.setIcon(custom_icon_45595205f9714201907adb1154e0da41);
        
    
            var marker_20a483a8dba0453db80c01621378a98a = L.marker(
                [-12.1426959, 39.9719042],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_73f335baaadd46e2a5f7ad8f4eb0b5ed = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_20a483a8dba0453db80c01621378a98a.setIcon(custom_icon_73f335baaadd46e2a5f7ad8f4eb0b5ed);
        
    
            var marker_d503911a73ed457bb623a8c310d23fa9 = L.marker(
                [-11.751388, 40.4312539],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_9a11676ab8d243fd888f96b4fb5d9690 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_d503911a73ed457bb623a8c310d23fa9.setIcon(custom_icon_9a11676ab8d243fd888f96b4fb5d9690);
        
    
            var marker_364db79e4ec9405187db19bebaef5cfe = L.marker(
                [-13.5468384, 38.4246451],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_b5a468366e0f49e19032f181411c0cc1 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_364db79e4ec9405187db19bebaef5cfe.setIcon(custom_icon_b5a468366e0f49e19032f181411c0cc1);
        
    
            var marker_ffd4590bdd634d27b2ab32ee2b65e973 = L.marker(
                [-13.8300362, 39.1229703],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_64b625e0970e48e3906847b0a825c49a = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_ffd4590bdd634d27b2ab32ee2b65e973.setIcon(custom_icon_64b625e0970e48e3906847b0a825c49a);
        
    
            var marker_5de924b80f214060b658578db68f718f = L.marker(
                [-13.3727186, 39.9681249],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_8ade7efed43b4feca6d142d5c12e0dd6 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_5de924b80f214060b658578db68f718f.setIcon(custom_icon_8ade7efed43b4feca6d142d5c12e0dd6);
        
    
            var marker_81e45eea91834a6ea0d159e0dfda527d = L.marker(
                [-11.5357956, 39.9366291],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_379457298b624fbea9eb08e8060c1a2a = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_81e45eea91834a6ea0d159e0dfda527d.setIcon(custom_icon_379457298b624fbea9eb08e8060c1a2a);
        
    
            var marker_6bba27840ef341d7a62adf73f0ab4ca6 = L.marker(
                [-11.7053046, 39.9854681],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_2959269dba8b4d28b6b0dfe16ebf09f6 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_6bba27840ef341d7a62adf73f0ab4ca6.setIcon(custom_icon_2959269dba8b4d28b6b0dfe16ebf09f6);
        
    
            var marker_e4462d31cd414bad899c946bd08d0bbe = L.marker(
                [-13.382453, 39.7843319],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_530e30ac85564ee69725fa1facb1f0a3 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_e4462d31cd414bad899c946bd08d0bbe.setIcon(custom_icon_530e30ac85564ee69725fa1facb1f0a3);
        
    
            var marker_d48210040fed489eb6608ef3ab31d9b0 = L.marker(
                [-13.3974148, 39.431714],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_e94600090c544b8c8f0d4ffb1deb53f2 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_d48210040fed489eb6608ef3ab31d9b0.setIcon(custom_icon_e94600090c544b8c8f0d4ffb1deb53f2);
        
    
            var marker_111eefaa36cf487d96aad3ac6e8ef453 = L.marker(
                [-11.2957627, 39.4423141],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_646cd903526646f093f3a15984454195 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_111eefaa36cf487d96aad3ac6e8ef453.setIcon(custom_icon_646cd903526646f093f3a15984454195);
        
    
            var marker_d468e51556de48deb2f19b4de41c1db4 = L.marker(
                [-13.9652029, 38.8055348],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ae098da66d324fbfa3369ba86ea4ce63 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_d468e51556de48deb2f19b4de41c1db4.setIcon(custom_icon_ae098da66d324fbfa3369ba86ea4ce63);
        
    
            var marker_06f41a9b45dc40f8a251d4856036db37 = L.marker(
                [-13.3778775, 38.37027],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_3da8c7d134a9452fa94f0fd57a334831 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_06f41a9b45dc40f8a251d4856036db37.setIcon(custom_icon_3da8c7d134a9452fa94f0fd57a334831);
        
    
            var marker_739372e30d0447dab1f4c614d204164b = L.marker(
                [-11.52996, 39.7185132],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_83b4516280304715802a7cbedd9f6174 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_739372e30d0447dab1f4c614d204164b.setIcon(custom_icon_83b4516280304715802a7cbedd9f6174);
        
    
            var marker_745072fc8331432e93e8069c283f9f6f = L.marker(
                [-11.6631353, 39.5535949],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_deb44c175b4f4c129bfe183e78f6e5c0 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_745072fc8331432e93e8069c283f9f6f.setIcon(custom_icon_deb44c175b4f4c129bfe183e78f6e5c0);
        
    
            var marker_da13fb506e2244c9ae1a06f45e626f8b = L.marker(
                [-13.3594985, 40.1934519],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_7515c917aa8a40249588bc5c3adc4614 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_da13fb506e2244c9ae1a06f45e626f8b.setIcon(custom_icon_7515c917aa8a40249588bc5c3adc4614);
        
    
            var marker_39ebd28b63704dd6af3925e2d84417ab = L.marker(
                [-11.3494398, 40.3583837],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_1a7f5d99cf5f492f91936d0610e5bfb1 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_39ebd28b63704dd6af3925e2d84417ab.setIcon(custom_icon_1a7f5d99cf5f492f91936d0610e5bfb1);
        
    
            var marker_0632a11d1b0d430fa83fb863d2ca3cd2 = L.marker(
                [-13.2233199, 38.8809907],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_e850de0c22124f2ab56954610ff61f99 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_0632a11d1b0d430fa83fb863d2ca3cd2.setIcon(custom_icon_e850de0c22124f2ab56954610ff61f99);
        
    
            var marker_5ff5dc573e6042258f11180b35899fc4 = L.marker(
                [-13.2260968, 38.4805879],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_0b04fdddf654458e99bbd66b6c186a5e = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_5ff5dc573e6042258f11180b35899fc4.setIcon(custom_icon_0b04fdddf654458e99bbd66b6c186a5e);
        
    
            var marker_01af20c437364f128866ff2ddac1a1b8 = L.marker(
                [-13.2908021, 40.5555984],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_0f5091c99db8422fb2eb9c48bdf88148 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_01af20c437364f128866ff2ddac1a1b8.setIcon(custom_icon_0f5091c99db8422fb2eb9c48bdf88148);
        
    
            var marker_9e98d8c8aa3547ab8b3425efbf06bd2a = L.marker(
                [-13.4743991, 39.1742098],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_5e378ba08a534a9cb824bf1a96896276 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_9e98d8c8aa3547ab8b3425efbf06bd2a.setIcon(custom_icon_5e378ba08a534a9cb824bf1a96896276);
        
    
            var marker_c44aec4ab87745c4b5d4941f650f2186 = L.marker(
                [-11.6268144, 40.1778884],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a74359a79127461287bb38f40477235a = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_c44aec4ab87745c4b5d4941f650f2186.setIcon(custom_icon_a74359a79127461287bb38f40477235a);
        
    
            var marker_d85a80fe56c742e2bd6c4706f266f184 = L.marker(
                [-13.1270182, 38.9984634],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ce87df5a455a4a7cac5d121d7e438fb1 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_d85a80fe56c742e2bd6c4706f266f184.setIcon(custom_icon_ce87df5a455a4a7cac5d121d7e438fb1);
        
    
            var marker_d72d37879ca94dbdbe1361e35f36ae76 = L.marker(
                [-12.2775973, 39.6643768],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_2c5f26776c6b4922b88581124270e159 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_d72d37879ca94dbdbe1361e35f36ae76.setIcon(custom_icon_2c5f26776c6b4922b88581124270e159);
        
    
            var marker_5152819f259e4472b61acba8602a9c81 = L.marker(
                [-12.9939627, 39.4675429],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_4fff076c33ef4b0eb10037b2e22b0883 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_5152819f259e4472b61acba8602a9c81.setIcon(custom_icon_4fff076c33ef4b0eb10037b2e22b0883);
        
    
            var marker_a0d15aae304b4ed9829e21eba42c26ea = L.marker(
                [-13.0319004, 39.5522001],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_4d2ff5273ed046538342c7a4c03799e5 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_a0d15aae304b4ed9829e21eba42c26ea.setIcon(custom_icon_4d2ff5273ed046538342c7a4c03799e5);
        
    
            var marker_59ff36b19bc04a73a96608056dc6c53c = L.marker(
                [-12.5403025, 39.6408096],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_db3acf0efa57428087ed5c0cad746d8e = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_59ff36b19bc04a73a96608056dc6c53c.setIcon(custom_icon_db3acf0efa57428087ed5c0cad746d8e);
        
    
            var marker_4b32cb8ec8dc4ea6b14317a5c57d22a3 = L.marker(
                [-13.104984, 39.8742181],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_7d69afe5b12a499fa81097bdb8a0c9d0 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_4b32cb8ec8dc4ea6b14317a5c57d22a3.setIcon(custom_icon_7d69afe5b12a499fa81097bdb8a0c9d0);
        
    
            var marker_e8be5cadbd814936982e604e74f4106d = L.marker(
                [-11.0613687, 39.6695977],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_7dcafa4b87f549bd9618a94a0ff3d4a0 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_e8be5cadbd814936982e604e74f4106d.setIcon(custom_icon_7dcafa4b87f549bd9618a94a0ff3d4a0);
        
    
            var marker_11c40eb5fb86433491f9d516cdbb09b3 = L.marker(
                [-13.1311036, 39.035596],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ca763f7edb4e4e9887d5a22983043383 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_11c40eb5fb86433491f9d516cdbb09b3.setIcon(custom_icon_ca763f7edb4e4e9887d5a22983043383);
        
    
            var marker_4d88c9850c7e45bda9492c0d672a9ef2 = L.marker(
                [-11.115467, 39.4739789],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ee85175fee1b47e7b4e870a3e5e88653 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_4d88c9850c7e45bda9492c0d672a9ef2.setIcon(custom_icon_ee85175fee1b47e7b4e870a3e5e88653);
        
    
            var marker_20a0dbc00542421387731689a7b60267 = L.marker(
                [-12.5506338, 39.0019047],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_c559a0f65b9b4280b193a0d44a5bc462 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_20a0dbc00542421387731689a7b60267.setIcon(custom_icon_c559a0f65b9b4280b193a0d44a5bc462);
        
    
            var marker_68db4dc11e974174b6c8416ad97a4e75 = L.marker(
                [-11.7792378, 39.900713],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_6dbfe45c96cf4585bcdd8395767c1577 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_68db4dc11e974174b6c8416ad97a4e75.setIcon(custom_icon_6dbfe45c96cf4585bcdd8395767c1577);
        
    
            var marker_de4c523c23a9468a8fbbec6aff22f12d = L.marker(
                [-12.9503254, 40.3197109],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_5076d8228c1a43dd9aa5215ed34f6d32 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_de4c523c23a9468a8fbbec6aff22f12d.setIcon(custom_icon_5076d8228c1a43dd9aa5215ed34f6d32);
        
    
            var marker_12690532628f43cd9075cfe1c682caf0 = L.marker(
                [-11.0740262, 39.6728942],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_4a68886b91dd4a608a25805c4f458113 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_12690532628f43cd9075cfe1c682caf0.setIcon(custom_icon_4a68886b91dd4a608a25805c4f458113);
        
    
            var marker_4bacce5e231947cf889ee32582959bd3 = L.marker(
                [-11.7601862, 39.8052947],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_f06a5a1018664ee597c93e6de6a010ee = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_4bacce5e231947cf889ee32582959bd3.setIcon(custom_icon_f06a5a1018664ee597c93e6de6a010ee);
        
    
            var marker_c9a836b4d02149c69f6170a22ac4140b = L.marker(
                [-11.6002997, 39.6841943],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a8780674e6f04bfb8e910895f3ca14cc = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_c9a836b4d02149c69f6170a22ac4140b.setIcon(custom_icon_a8780674e6f04bfb8e910895f3ca14cc);
        
    
            var marker_59e752a1a272404a99358074c0550b9b = L.marker(
                [-13.4835673, 39.9148697],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_025ff458a6db4091a9b2ec8d760d8a52 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_59e752a1a272404a99358074c0550b9b.setIcon(custom_icon_025ff458a6db4091a9b2ec8d760d8a52);
        
    
            var marker_5a277f56de534793b477f37d28e0fac5 = L.marker(
                [-13.1281036, 38.9989047],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_4f134ee60ef04554867c092323152def = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_5a277f56de534793b477f37d28e0fac5.setIcon(custom_icon_4f134ee60ef04554867c092323152def);
        
    
            var marker_cb905cf93e1c4278a139615e4f0ab512 = L.marker(
                [-11.7612458, 39.7356418],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_6141209bc3dc483fbc63f32ae72f001f = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_cb905cf93e1c4278a139615e4f0ab512.setIcon(custom_icon_6141209bc3dc483fbc63f32ae72f001f);
        
    
            var marker_a132ceea5f2f49848e9be6bc93b4725e = L.marker(
                [-11.3057732, 39.3102796],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_9136e676aa154079b90be26f9e68f2e9 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_a132ceea5f2f49848e9be6bc93b4725e.setIcon(custom_icon_9136e676aa154079b90be26f9e68f2e9);
        
    
            var marker_ae209b16a57241ddbceb79b06db59137 = L.marker(
                [-13.6187109, 38.8164917],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_6112fc46b3e449df880bb54c04a02167 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_ae209b16a57241ddbceb79b06db59137.setIcon(custom_icon_6112fc46b3e449df880bb54c04a02167);
        
    
            var marker_b501155e33884a92ad762fb46c75ce9b = L.marker(
                [-13.3480551, 38.5669295],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_420687c844a44f3694996afe7a0e87f0 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_b501155e33884a92ad762fb46c75ce9b.setIcon(custom_icon_420687c844a44f3694996afe7a0e87f0);
        
    
            var marker_bc5b91a5cf1840edbd4da96d119a4e9d = L.marker(
                [-12.563815, 40.2852472],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_71a67a614da8409bb2a7751242abb7df = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_bc5b91a5cf1840edbd4da96d119a4e9d.setIcon(custom_icon_71a67a614da8409bb2a7751242abb7df);
        
    
            var marker_4757468236da4f3cb05d9f99789560d1 = L.marker(
                [-13.3292302, 40.1008594],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_3baad037f4434f5bb79c02fb78a1b6ef = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_4757468236da4f3cb05d9f99789560d1.setIcon(custom_icon_3baad037f4434f5bb79c02fb78a1b6ef);
        
    
            var marker_6773de7502fb4713a04a930f44b9b98d = L.marker(
                [-12.966889, 39.8570546],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_cf4b6d1a5929471594c2703993775927 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_6773de7502fb4713a04a930f44b9b98d.setIcon(custom_icon_cf4b6d1a5929471594c2703993775927);
        
    
            var marker_b30d1f7b539c414d88e6d9d0b8400acd = L.marker(
                [-11.822572, 39.4167834],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ed40e5e623b34835aa3768c11398c264 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_b30d1f7b539c414d88e6d9d0b8400acd.setIcon(custom_icon_ed40e5e623b34835aa3768c11398c264);
        
    
            var marker_06467dd21cf54453a89797a0e9c3fc10 = L.marker(
                [-13.428525, 38.5947065],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a70f5b17becf48f7ab63d98e77df9387 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_06467dd21cf54453a89797a0e9c3fc10.setIcon(custom_icon_a70f5b17becf48f7ab63d98e77df9387);
        
    
            var marker_e13e143408504245a597e8912a956d5f = L.marker(
                [-13.2734008, 38.6361238],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_3381255dd69b45a7b42dd4b42c37c191 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_e13e143408504245a597e8912a956d5f.setIcon(custom_icon_3381255dd69b45a7b42dd4b42c37c191);
        
    
            var marker_502ae444a9c7401ca6df5943d5af3966 = L.marker(
                [-10.8568725, 40.5894318],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_b220e7e168264994a84b4c97335a64bf = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_502ae444a9c7401ca6df5943d5af3966.setIcon(custom_icon_b220e7e168264994a84b4c97335a64bf);
        
    
            var marker_94ecfece91014c58bddc80b5e724f37d = L.marker(
                [-13.0916136, 39.5930985],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_b3bfa54e61964ce09e45d284138f8a0c = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_94ecfece91014c58bddc80b5e724f37d.setIcon(custom_icon_b3bfa54e61964ce09e45d284138f8a0c);
        
    
            var marker_20cb8bed71be414fa0643c21cd34b6ca = L.marker(
                [-10.5929141, 40.5078122],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_aaffe23709c64797beaabc644049a02f = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_20cb8bed71be414fa0643c21cd34b6ca.setIcon(custom_icon_aaffe23709c64797beaabc644049a02f);
        
    
            var marker_a8c8feee4d0543f4bc34bfdb2910cd8f = L.marker(
                [-13.688018, 38.7754324],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_aca6699745704f9c86513f573c80edb4 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_a8c8feee4d0543f4bc34bfdb2910cd8f.setIcon(custom_icon_aca6699745704f9c86513f573c80edb4);
        
    
            var marker_148a9a5bf44d46bfa8b825c34ba069ce = L.marker(
                [-13.4165852, 40.5266963],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a98becab12e94f58902ebf2567114ee9 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_148a9a5bf44d46bfa8b825c34ba069ce.setIcon(custom_icon_a98becab12e94f58902ebf2567114ee9);
        
    
            var marker_82e997bde6884e9d89953b1a1cbf08ef = L.marker(
                [-11.8237797, 39.812306],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_1950720f8dcb47d89fa37b876726faa3 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_82e997bde6884e9d89953b1a1cbf08ef.setIcon(custom_icon_1950720f8dcb47d89fa37b876726faa3);
        
    
            var marker_73d3f14fb27d4ff3987fce9b1822eaaa = L.marker(
                [-10.9648432, 40.3559308],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_19a6159ae0ec4e10b4074e34733eaffc = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_73d3f14fb27d4ff3987fce9b1822eaaa.setIcon(custom_icon_19a6159ae0ec4e10b4074e34733eaffc);
        
    
            var marker_e06ae189ffc8489b8c29dbcee6a99ab9 = L.marker(
                [-12.5431851, 39.6440323],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_902b7cff691841ba99a4d929709864d2 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_e06ae189ffc8489b8c29dbcee6a99ab9.setIcon(custom_icon_902b7cff691841ba99a4d929709864d2);
        
    
            var marker_aba0ed34dd574bbc86988cbd15529a88 = L.marker(
                [-12.5958119, 40.1522794],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_451bfe6397d1445f9b42e664c31825ed = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_aba0ed34dd574bbc86988cbd15529a88.setIcon(custom_icon_451bfe6397d1445f9b42e664c31825ed);
        
    
            var marker_efe4e596bcab4a49a1e4b3420a7f92e2 = L.marker(
                [-11.2307631, 40.2729017],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_24fb9e1cd16a49f39f55fc35cfaca89a = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_efe4e596bcab4a49a1e4b3420a7f92e2.setIcon(custom_icon_24fb9e1cd16a49f39f55fc35cfaca89a);
        
    
            var marker_9459e6460d03409da536cc65db3564c0 = L.marker(
                [-10.8907332, 40.05759],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_d3c931defb8b42bc939579dfcb572f19 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_9459e6460d03409da536cc65db3564c0.setIcon(custom_icon_d3c931defb8b42bc939579dfcb572f19);
        
    
            var marker_fc95fad90c704e5ab3fa22e3e5a0e1d7 = L.marker(
                [-10.7810295, 40.4730803],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_0e54bae9abb74a169de08a16dbdf4a89 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_fc95fad90c704e5ab3fa22e3e5a0e1d7.setIcon(custom_icon_0e54bae9abb74a169de08a16dbdf4a89);
        
    
            var marker_cb6e2cbbfffd404d99dd2c4cbee797f9 = L.marker(
                [-14.0363222, 38.6765823],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_741ce8d6adf440c3a2809929068e99fe = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_cb6e2cbbfffd404d99dd2c4cbee797f9.setIcon(custom_icon_741ce8d6adf440c3a2809929068e99fe);
        
    
            var marker_e31216ce3f044c3f9c393f2ebad62dad = L.marker(
                [-13.6460298, 39.7932637],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_cbd6cf2c791842ecabd83d04227a3bd0 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_e31216ce3f044c3f9c393f2ebad62dad.setIcon(custom_icon_cbd6cf2c791842ecabd83d04227a3bd0);
        
    
            var marker_3ab756ea26ef4a02920443bd29331f7c = L.marker(
                [-10.9903293, 40.4792212],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_49b1a4e6e8b346cda189543f4d75c4bb = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_3ab756ea26ef4a02920443bd29331f7c.setIcon(custom_icon_49b1a4e6e8b346cda189543f4d75c4bb);
        
    
            var marker_bfdef978032d4550817d23fea5ebcc09 = L.marker(
                [-11.3864065, 39.5948687],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_23616e5c87274f6297920f913c76564e = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_bfdef978032d4550817d23fea5ebcc09.setIcon(custom_icon_23616e5c87274f6297920f913c76564e);
        
    
            var marker_b5b337193dc74a36b90bbd189ddaacfa = L.marker(
                [-13.1886069, 38.7432043],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_3dd76ab60d93450893a381098d4c0bd8 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_b5b337193dc74a36b90bbd189ddaacfa.setIcon(custom_icon_3dd76ab60d93450893a381098d4c0bd8);
        
    
            var marker_da217c4e1c44491db2783e2ca9a26001 = L.marker(
                [-11.4266587, 39.7414233],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_60fea8efbc954efc8e7daf7869ad1ad4 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_da217c4e1c44491db2783e2ca9a26001.setIcon(custom_icon_60fea8efbc954efc8e7daf7869ad1ad4);
        
    
            var marker_f17ddd13c1584e609340baa1f8130b09 = L.marker(
                [-13.1168099, 38.9999105],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_23c025c77a0c475580a582de60de40c9 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_f17ddd13c1584e609340baa1f8130b09.setIcon(custom_icon_23c025c77a0c475580a582de60de40c9);
        
    
            var marker_86607b23ac234d0db1760bb06df59bf2 = L.marker(
                [-12.8601364, 39.9489686],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_edc5b52294bc4089a89b812c3433136e = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_86607b23ac234d0db1760bb06df59bf2.setIcon(custom_icon_edc5b52294bc4089a89b812c3433136e);
        
    
            var marker_340fc04bf63c44c39ef1a74ae82e3b6c = L.marker(
                [-13.7094725, 38.6005551],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_b681fb0f36154f75bce3051e9b8c8189 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_340fc04bf63c44c39ef1a74ae82e3b6c.setIcon(custom_icon_b681fb0f36154f75bce3051e9b8c8189);
        
    
            var marker_2016dddb24aa4e0a9105471a67b30478 = L.marker(
                [-12.4590882, 40.029164],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_5c72b8c5849b411a945b6a957d8e7a75 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_2016dddb24aa4e0a9105471a67b30478.setIcon(custom_icon_5c72b8c5849b411a945b6a957d8e7a75);
        
    
            var marker_946bee6625dc4782b21c75980035534a = L.marker(
                [-12.9679829, 38.801301],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ae8367622fa84bcf8f1c70085b3379d9 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_946bee6625dc4782b21c75980035534a.setIcon(custom_icon_ae8367622fa84bcf8f1c70085b3379d9);
        
    
            var marker_b6198111a88643949bfe84862fb9c04f = L.marker(
                [-17.1243924, 33.290024],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_92cd842bcb6e4aa9a1e919ede0c7820b = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_b6198111a88643949bfe84862fb9c04f.setIcon(custom_icon_92cd842bcb6e4aa9a1e919ede0c7820b);
        
    
            var marker_82ef91f53252469ab9a76fc53c5275e4 = L.marker(
                [-18.0762961, 36.9277793],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a78f3be2ffb84e1a929903b573241272 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_82ef91f53252469ab9a76fc53c5275e4.setIcon(custom_icon_a78f3be2ffb84e1a929903b573241272);
        
    
            var marker_9839d7a0ab504c18836479cd1f917923 = L.marker(
                [-16.8566653, 33.2901688],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_9bd8a9ff076e4bc0892a640ab0c32a6f = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_9839d7a0ab504c18836479cd1f917923.setIcon(custom_icon_9bd8a9ff076e4bc0892a640ab0c32a6f);
        
    
            var marker_c483429e7c23403e9f13aa4535df53ae = L.marker(
                [-17.3299024, 37.1996722],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_360a830732d04e989a647e84cdc37606 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_c483429e7c23403e9f13aa4535df53ae.setIcon(custom_icon_360a830732d04e989a647e84cdc37606);
        
    
            var marker_302469cdf03b4aa38d41639db11363c4 = L.marker(
                [-23.8521996, 34.9310989],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_9ea7457d7b78414481a3e5fb6e344177 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_302469cdf03b4aa38d41639db11363c4.setIcon(custom_icon_9ea7457d7b78414481a3e5fb6e344177);
        
    
            var marker_ea9e2b5c21a94517b241bf5a9758209e = L.marker(
                [-18.2684168, 36.6500714],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_cbf446d061024090b871a6e04f7cbdc3 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_ea9e2b5c21a94517b241bf5a9758209e.setIcon(custom_icon_cbf446d061024090b871a6e04f7cbdc3);
        
    
            var marker_7e6082d28c68403791ec38889c4a4d3b = L.marker(
                [-20.0998976, 33.0957636],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_23ade8741d514b47ace046af4a06f04d = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_7e6082d28c68403791ec38889c4a4d3b.setIcon(custom_icon_23ade8741d514b47ace046af4a06f04d);
        
    
            var marker_6e9acad84a1f4cf892267360a471bfe8 = L.marker(
                [-19.3137126, 32.9442859],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_91cfa01ed81c4bd9a90ab1f2e9618f28 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_6e9acad84a1f4cf892267360a471bfe8.setIcon(custom_icon_91cfa01ed81c4bd9a90ab1f2e9618f28);
        
    
            var marker_7975624ece49498485e5b3727b3ba910 = L.marker(
                [-16.7245811, 34.2451814],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_86ae871d07a24c539f594133576cb956 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_7975624ece49498485e5b3727b3ba910.setIcon(custom_icon_86ae871d07a24c539f594133576cb956);
        
    
            var marker_85f6e0cc1c8d4091b1f23db1aa804746 = L.marker(
                [-16.9673139, 38.0493464],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_0c67bc95c991474287e3b204c0b89c65 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_85f6e0cc1c8d4091b1f23db1aa804746.setIcon(custom_icon_0c67bc95c991474287e3b204c0b89c65);
        
    
            var marker_b715539286e74023b01fd4395ddbdc7f = L.marker(
                [-20.2278154, 33.3295171],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_593bbca437ce469aa2bc4c40c26354fe = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_b715539286e74023b01fd4395ddbdc7f.setIcon(custom_icon_593bbca437ce469aa2bc4c40c26354fe);
        
    
            var marker_71b5a6fdc83141f4a94dc30781f964e5 = L.marker(
                [-26.8371857, 32.8842379],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_879b8983e85f4650a4f0fd156b77c0a0 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_71b5a6fdc83141f4a94dc30781f964e5.setIcon(custom_icon_879b8983e85f4650a4f0fd156b77c0a0);
        
    
            var marker_17a4f1f2cdbd443aa371be7463694dd9 = L.marker(
                [-25.9741898, 32.5831718],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_0599c92cfcf54a8985d58dbf92cfc3f2 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_17a4f1f2cdbd443aa371be7463694dd9.setIcon(custom_icon_0599c92cfcf54a8985d58dbf92cfc3f2);
        
    
            var marker_e94ca78ba4a84f1787f6fbdd20200be4 = L.marker(
                [-25.5643925, 32.7994452],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_1e1d7debdc74402c9f4a2de8dde8037d = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_e94ca78ba4a84f1787f6fbdd20200be4.setIcon(custom_icon_1e1d7debdc74402c9f4a2de8dde8037d);
        
    
            var marker_7ea9e9f8f513441abe6a09dae3eca077 = L.marker(
                [-17.9358696, 36.9431484],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_b64ce566ad644271a6fd8131f91fcf7c = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_7ea9e9f8f513441abe6a09dae3eca077.setIcon(custom_icon_b64ce566ad644271a6fd8131f91fcf7c);
        
    
            var marker_c0892c5fdf5a42a486b83d608141bebb = L.marker(
                [-18.6655513, 36.2424253],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_09540daa545c4080ac32e54d2f84c7b0 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_c0892c5fdf5a42a486b83d608141bebb.setIcon(custom_icon_09540daa545c4080ac32e54d2f84c7b0);
        
    
            var marker_a6b6fe293b2a4c3d9caf9980ef35c945 = L.marker(
                [-16.2728031, 38.2549886],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_eb932dddbfad49d89e0ccd34df492d43 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_a6b6fe293b2a4c3d9caf9980ef35c945.setIcon(custom_icon_eb932dddbfad49d89e0ccd34df492d43);
        
    
            var marker_61c9022db2184c50b4dc39fb1dff64a3 = L.marker(
                [-18.0101226, 36.8107745],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_86d5229a7aa1478ea716502ffeb27cdc = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_61c9022db2184c50b4dc39fb1dff64a3.setIcon(custom_icon_86d5229a7aa1478ea716502ffeb27cdc);
        
    
            var marker_89dfd8673a7f4c319ab350df9c1cf908 = L.marker(
                [-18.8163607, 33.038216],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_984fc5c18fe645f493fc9a739e0bc188 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_89dfd8673a7f4c319ab350df9c1cf908.setIcon(custom_icon_984fc5c18fe645f493fc9a739e0bc188);
        
    
            var marker_c171770deb5a499a9d384f1ca1252512 = L.marker(
                [-16.4490722, 36.0462614],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_611ceb327c324ee6be1ba0fe67bac392 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_c171770deb5a499a9d384f1ca1252512.setIcon(custom_icon_611ceb327c324ee6be1ba0fe67bac392);
        
    
            var marker_7ec04ad7025246cc8f399e6b5503e11f = L.marker(
                [-21.0262191, 33.5356457],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_9c66af62c9454966abdcf63192d99cf7 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_7ec04ad7025246cc8f399e6b5503e11f.setIcon(custom_icon_9c66af62c9454966abdcf63192d99cf7);
        
    
            var marker_469b59c68004486ebea7b4312a0921bf = L.marker(
                [-14.8495153, 34.5276352],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_2f4a9b9d8e8e4e7baf788797dfee033d = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_469b59c68004486ebea7b4312a0921bf.setIcon(custom_icon_2f4a9b9d8e8e4e7baf788797dfee033d);
        
    
            var marker_396abdcec78c4e67b746e2f526463311 = L.marker(
                [-17.2514319, 34.1780692],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_fd37ab38e0b54764b2dcf017bdb4a2e8 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_396abdcec78c4e67b746e2f526463311.setIcon(custom_icon_fd37ab38e0b54764b2dcf017bdb4a2e8);
        
    
            var marker_5c077795d29c48c48403bdbf5489fd47 = L.marker(
                [-20.9545728, 33.2723495],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_2f055dee14c045e8b09214199cedd6cd = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_5c077795d29c48c48403bdbf5489fd47.setIcon(custom_icon_2f055dee14c045e8b09214199cedd6cd);
        
    
            var marker_33137d7795ed4b70ac057264664f65ab = L.marker(
                [-19.0998731, 33.8100064],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_359a4372029146b6a3287d8a36c69cce = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_33137d7795ed4b70ac057264664f65ab.setIcon(custom_icon_359a4372029146b6a3287d8a36c69cce);
        
    
            var marker_f456a3187efc4b85b4e9b6209e3c168b = L.marker(
                [-14.7229721, 40.0686461],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_98c657d817834e238641c910f6f5b21d = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_f456a3187efc4b85b4e9b6209e3c168b.setIcon(custom_icon_98c657d817834e238641c910f6f5b21d);
        
    
            var marker_b61bdb5689604d89a51552d8fa8b7d6d = L.marker(
                [-22.0240135, 34.1446178],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_433ccf3991454f07a4bdb4c9a06e5ac2 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_b61bdb5689604d89a51552d8fa8b7d6d.setIcon(custom_icon_433ccf3991454f07a4bdb4c9a06e5ac2);
        
    
            var marker_7d38531f2cab4edb87a081cf424f43a4 = L.marker(
                [-21.8494911, 34.4794273],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_c40f91d9056d47bd92982eb30b6159af = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_7d38531f2cab4edb87a081cf424f43a4.setIcon(custom_icon_c40f91d9056d47bd92982eb30b6159af);
        
    
            var marker_dbd434f5b4de461693021e29ecc97d13 = L.marker(
                [-23.4393323, 35.2334504],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ad4db25a9c6e4538998105af8596c828 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_dbd434f5b4de461693021e29ecc97d13.setIcon(custom_icon_ad4db25a9c6e4538998105af8596c828);
        
    
            var marker_8537fb074a9d4e0e856d15a287c316cf = L.marker(
                [-16.557002, 37.2924351],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_acbad3a2afaa465086e8acedd9be0bf7 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_8537fb074a9d4e0e856d15a287c316cf.setIcon(custom_icon_acbad3a2afaa465086e8acedd9be0bf7);
        
    
            var marker_7d055c2ed31040d19ee82d10c9a26b15 = L.marker(
                [-15.5566946, 37.0553393],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_2249d27d46e14fb5ab11fb49ff76aac3 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_7d055c2ed31040d19ee82d10c9a26b15.setIcon(custom_icon_2249d27d46e14fb5ab11fb49ff76aac3);
        
    
            var marker_c772e2fbfe0f4d7c80e9cbfd4e9bdd06 = L.marker(
                [-18.0291843, 36.7362213],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_b88ddd23b090427cac9ec483640b72b5 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_c772e2fbfe0f4d7c80e9cbfd4e9bdd06.setIcon(custom_icon_b88ddd23b090427cac9ec483640b72b5);
        
    
            var marker_0c91e52ce3294696bd9d7da734dc0253 = L.marker(
                [-21.4581505, 32.9136467],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_b530e3b74a62449db4f1e2a67de74479 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_0c91e52ce3294696bd9d7da734dc0253.setIcon(custom_icon_b530e3b74a62449db4f1e2a67de74479);
        
    
            var marker_63404aa077db495980891af29b3ca9c9 = L.marker(
                [-14.1794943, 40.5249582],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_14a3fd1d83c94ce493fdf7bb8ac7a841 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_63404aa077db495980891af29b3ca9c9.setIcon(custom_icon_14a3fd1d83c94ce493fdf7bb8ac7a841);
        
    
            var marker_38a0eb7147dd4fb7af9c4028d8a2793b = L.marker(
                [-17.3091696, 37.9742736],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_7b2cf354f2104a51823e5475d7fa3d8e = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_38a0eb7147dd4fb7af9c4028d8a2793b.setIcon(custom_icon_7b2cf354f2104a51823e5475d7fa3d8e);
        
    
            var marker_9ded8f4f0ff84711a816f59e353754b4 = L.marker(
                [-17.3176417, 34.28176],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_1528575c3e0f458597608c486dd3359c = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_9ded8f4f0ff84711a816f59e353754b4.setIcon(custom_icon_1528575c3e0f458597608c486dd3359c);
        
    
            var marker_14f9785589e24e30b8e89b2470bc0146 = L.marker(
                [-14.0194702, 40.3455251],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_4501f67b05ec4cb9bc0e5d0c2dcae07d = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_14f9785589e24e30b8e89b2470bc0146.setIcon(custom_icon_4501f67b05ec4cb9bc0e5d0c2dcae07d);
        
    
            var marker_56533ac53e60428d80e4d85c4f64bc5f = L.marker(
                [-19.2644475, 33.38777],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_10ef870b55784efd9764dc4c338726ea = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_56533ac53e60428d80e4d85c4f64bc5f.setIcon(custom_icon_10ef870b55784efd9764dc4c338726ea);
        
    
            var marker_2a05ed498af14b90bebd5dff64c1f8f4 = L.marker(
                [-26.2959616, 32.1877621],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_0f4e3ccbca4440ea9b23e554cdab5f08 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_2a05ed498af14b90bebd5dff64c1f8f4.setIcon(custom_icon_0f4e3ccbca4440ea9b23e554cdab5f08);
        
    
            var marker_45373aa27792446f878f8b126e8a996a = L.marker(
                [-25.1791994, 32.8521238],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_0b414ee148364a9d963c35879c5a30cc = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_45373aa27792446f878f8b126e8a996a.setIcon(custom_icon_0b414ee148364a9d963c35879c5a30cc);
        
    
            var marker_8761a24908ec49d5b15284eb0e46e1c3 = L.marker(
                [-25.9600276, 32.4172345],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_863ed2b5279348d5bb9b40bac767ac8c = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_8761a24908ec49d5b15284eb0e46e1c3.setIcon(custom_icon_863ed2b5279348d5bb9b40bac767ac8c);
        
    
            var marker_259586dae97b459f98fed2a657000d01 = L.marker(
                [-26.2014734, 32.1388534],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_d66222db3fa94fa3b8f99398b4359355 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_259586dae97b459f98fed2a657000d01.setIcon(custom_icon_d66222db3fa94fa3b8f99398b4359355);
        
    
            var marker_3b9eb75a286d4c38b29ca6c861639127 = L.marker(
                [-25.2849373, 32.5120774],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_927c8ae6df9c41e4b8970cf2ca7b3a43 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_3b9eb75a286d4c38b29ca6c861639127.setIcon(custom_icon_927c8ae6df9c41e4b8970cf2ca7b3a43);
        
    
            var marker_9e977935a8114466b3a9392f8a3a7771 = L.marker(
                [-25.353414, 32.9335919],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_853d2b610d544bad9575e7fee2c539da = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_9e977935a8114466b3a9392f8a3a7771.setIcon(custom_icon_853d2b610d544bad9575e7fee2c539da);
        
    
            var marker_36c3f3700972422c867ca72cb0d34efb = L.marker(
                [-26.0647897, 32.2864151],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_35d9c87bf9204dd1b19c2ce8ebaa78e1 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_36c3f3700972422c867ca72cb0d34efb.setIcon(custom_icon_35d9c87bf9204dd1b19c2ce8ebaa78e1);
        
    
            var marker_82fc70390a8c4b4f82934bd9fc6e1916 = L.marker(
                [-26.3684366, 32.6187408],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_7e2c51316a6f466580231ad7633616f3 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_82fc70390a8c4b4f82934bd9fc6e1916.setIcon(custom_icon_7e2c51316a6f466580231ad7633616f3);
        
    
            var marker_762d5918a75e4d63a72328059fb32cb8 = L.marker(
                [-26.0885194, 32.2598438],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a3520c5aada44b47b4f85ae7b641b3a6 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_762d5918a75e4d63a72328059fb32cb8.setIcon(custom_icon_a3520c5aada44b47b4f85ae7b641b3a6);
        
    
            var marker_20093ea0c2f04001aa87bd554dc6a18a = L.marker(
                [-26.0468815, 32.3351911],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_94992210172c41c9886847443ad8485c = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_20093ea0c2f04001aa87bd554dc6a18a.setIcon(custom_icon_94992210172c41c9886847443ad8485c);
        
    
            var marker_019767f6ee6942529089bf3eb54a41c0 = L.marker(
                [-15.3002254, 39.8703074],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_90749439757e4064b87390066fd5d197 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_019767f6ee6942529089bf3eb54a41c0.setIcon(custom_icon_90749439757e4064b87390066fd5d197);
        
    
            var marker_6811024302204ea8bca36ed11d8574c7 = L.marker(
                [-17.0473162, 33.6921668],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_23e069a927c844ffb8304817ade6b00c = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_6811024302204ea8bca36ed11d8574c7.setIcon(custom_icon_23e069a927c844ffb8304817ade6b00c);
        
    
            var marker_06586d911a784a4b867006d6830e83ec = L.marker(
                [-18.953468, 33.2648493],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_bac486ae2014450689b7cb30bcd7b380 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_06586d911a784a4b867006d6830e83ec.setIcon(custom_icon_bac486ae2014450689b7cb30bcd7b380);
        
    
            var marker_93347a112c7843918c8bd3e3a24bb689 = L.marker(
                [-19.1010326, 32.9952934],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_854c519bdbf24897ae55e78c03911d51 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_93347a112c7843918c8bd3e3a24bb689.setIcon(custom_icon_854c519bdbf24897ae55e78c03911d51);
        
    
            var marker_72a6bd4b0ade4454ab3981feb3222fd5 = L.marker(
                [-17.7848141, 36.8106043],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a8a1ae3687d941a6b06f0592ce0e6e67 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_72a6bd4b0ade4454ab3981feb3222fd5.setIcon(custom_icon_a8a1ae3687d941a6b06f0592ce0e6e67);
        
    
            var marker_e35a3f58c330426f8772ba6fd018e249 = L.marker(
                [-17.7846991, 35.4057194],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_58475bbe31544a3fadc96dec5c3cc346 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_e35a3f58c330426f8772ba6fd018e249.setIcon(custom_icon_58475bbe31544a3fadc96dec5c3cc346);
        
    
            var marker_a857b0b1476e4675bdf947fd41e3bb6f = L.marker(
                [-18.9754165, 32.8258143],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ceee3ad4971b4a9591296783167cdfa3 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_a857b0b1476e4675bdf947fd41e3bb6f.setIcon(custom_icon_ceee3ad4971b4a9591296783167cdfa3);
        
    
            var marker_08f3c39c8fc64735870f2f84457304b5 = L.marker(
                [-15.6709486, 39.4599052],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_c61c64c3d69440359d37c27d1cce99a0 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_08f3c39c8fc64735870f2f84457304b5.setIcon(custom_icon_c61c64c3d69440359d37c27d1cce99a0);
        
    
            var marker_6cd2f80c86234a50910a2479934cbb20 = L.marker(
                [-17.7003175, 37.1130422],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_77a78131350545a8b0701552db3c307b = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_6cd2f80c86234a50910a2479934cbb20.setIcon(custom_icon_77a78131350545a8b0701552db3c307b);
        
    
            var marker_0ed70ffbd76d44a89c6e95f0a287991a = L.marker(
                [-20.3197974, 32.994139],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_71ec542bacfe475fb0236467e8ac241f = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_0ed70ffbd76d44a89c6e95f0a287991a.setIcon(custom_icon_71ec542bacfe475fb0236467e8ac241f);
        
    
            var marker_83c34ecd23d94948948bd357433be1fb = L.marker(
                [-19.1511633, 33.6609886],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_31d6c1d85968499b9e278c6fee699e7d = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_83c34ecd23d94948948bd357433be1fb.setIcon(custom_icon_31d6c1d85968499b9e278c6fee699e7d);
        
    
            var marker_feb4215987854f14af5ac514e62828f1 = L.marker(
                [-18.9994076, 33.3859654],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_00c700b9610b44289b5d7d77bd8cc39d = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_feb4215987854f14af5ac514e62828f1.setIcon(custom_icon_00c700b9610b44289b5d7d77bd8cc39d);
        
    
            var marker_a60be8b425784314860a8489f57896d1 = L.marker(
                [-17.690508, 35.6659466],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_8ff7339a49964805b885ad2f18e82ff0 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_a60be8b425784314860a8489f57896d1.setIcon(custom_icon_8ff7339a49964805b885ad2f18e82ff0);
        
    
            var marker_46b0f05e404e4490addafbb239e83036 = L.marker(
                [-16.2506332, 39.6526247],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_90db9126db034e0390006aef6285c01a = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_46b0f05e404e4490addafbb239e83036.setIcon(custom_icon_90db9126db034e0390006aef6285c01a);
        
    
            var marker_ea5e4fa12f6948eeac86fc218c28f692 = L.marker(
                [-23.2968522, 35.1348181],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_345b07830c4948d7a2b15dfb30f7a5de = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_ea5e4fa12f6948eeac86fc218c28f692.setIcon(custom_icon_345b07830c4948d7a2b15dfb30f7a5de);
        
    
            var marker_475c6a04908049b69e414f391fbc67a4 = L.marker(
                [-23.8811245, 35.152949],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a042d35db263489aaf57277c218ad91a = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_475c6a04908049b69e414f391fbc67a4.setIcon(custom_icon_a042d35db263489aaf57277c218ad91a);
        
    
            var marker_9628fcb548524e2f960c71c3fc2fa606 = L.marker(
                [-23.1721722, 35.0585722],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_4a58257bdbdd46808a7773c8a9e12284 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_9628fcb548524e2f960c71c3fc2fa606.setIcon(custom_icon_4a58257bdbdd46808a7773c8a9e12284);
        
    
            var marker_f77cc9089a1d4f6699270322a8a591f7 = L.marker(
                [-24.2652553, 35.2373535],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_33ee9751a36b4e2591ce979fc02ce7e1 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_f77cc9089a1d4f6699270322a8a591f7.setIcon(custom_icon_33ee9751a36b4e2591ce979fc02ce7e1);
        
    
            var marker_b86cbf8d106c41ebb89826722d683118 = L.marker(
                [-22.3101326, 35.4264646],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_6acba0757db54f63aae8232f29d08c18 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_b86cbf8d106c41ebb89826722d683118.setIcon(custom_icon_6acba0757db54f63aae8232f29d08c18);
        
    
            var marker_0a1632e01cf84aaaa7513f3a8e5a0df5 = L.marker(
                [-23.6561976, 35.3422373],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_865aa378d460450b84d069d5f7df3093 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_0a1632e01cf84aaaa7513f3a8e5a0df5.setIcon(custom_icon_865aa378d460450b84d069d5f7df3093);
        
    
            var marker_3b409504ea6044c38aec5e6725839be9 = L.marker(
                [-23.8174372, 35.3044648],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_c07ba2d3f20d49438f2e69c203fcb0fb = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_3b409504ea6044c38aec5e6725839be9.setIcon(custom_icon_c07ba2d3f20d49438f2e69c203fcb0fb);
        
    
            var marker_1e0616ef556644b9b255cafcec72f458 = L.marker(
                [-23.7698587, 35.2789503],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_b72c61cbca4644d88608bcca1bd04658 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_1e0616ef556644b9b255cafcec72f458.setIcon(custom_icon_b72c61cbca4644d88608bcca1bd04658);
        
    
            var marker_9ac784d5bf2f40aa912d74c167e85b96 = L.marker(
                [-23.8761647, 35.0415137],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_d7dc5a3a6b804a70a41cdf76daf07903 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_9ac784d5bf2f40aa912d74c167e85b96.setIcon(custom_icon_d7dc5a3a6b804a70a41cdf76daf07903);
        
    
            var marker_06468bed16dc4b7f97cad8506aa09bc0 = L.marker(
                [-24.1109726, 35.3178417],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_5970132141c94f0fbe6752f9d83a4230 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_06468bed16dc4b7f97cad8506aa09bc0.setIcon(custom_icon_5970132141c94f0fbe6752f9d83a4230);
        
    
            var marker_be46e9e8b6454630bfe4544b4de9e75b = L.marker(
                [-23.8829123, 35.1520295],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_24daac54eb8d439a8928cd78428dbaca = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_be46e9e8b6454630bfe4544b4de9e75b.setIcon(custom_icon_24daac54eb8d439a8928cd78428dbaca);
        
    
            var marker_af8afcc7f6ac40cb9a45d32d738fe424 = L.marker(
                [-23.8810828, 35.1529772],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_c73373135d734b47a9ddb07b5a2ddebe = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_af8afcc7f6ac40cb9a45d32d738fe424.setIcon(custom_icon_c73373135d734b47a9ddb07b5a2ddebe);
        
    
            var marker_daa5ce09dc4b4d62a395b7c87849301a = L.marker(
                [-24.1446158, 35.2176908],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_6d6de43efb334b2b9df95a63a73b4656 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_daa5ce09dc4b4d62a395b7c87849301a.setIcon(custom_icon_6d6de43efb334b2b9df95a63a73b4656);
        
    
            var marker_8ac74101588e4b8ca1f4e449e07751e6 = L.marker(
                [-23.8618884, 35.343202],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_406cebb20b9c495fb83ef76e737a640f = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_8ac74101588e4b8ca1f4e449e07751e6.setIcon(custom_icon_406cebb20b9c495fb83ef76e737a640f);
        
    
            var marker_b24c9e2f59fa4c89b1095248c66c2219 = L.marker(
                [-23.7171175, 35.3617809],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_731a55861b464d9ea1207aab42902a38 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_b24c9e2f59fa4c89b1095248c66c2219.setIcon(custom_icon_731a55861b464d9ea1207aab42902a38);
        
    
            var marker_7bb1aa5ee50e40b5a3fdfcb3dfe4b144 = L.marker(
                [-23.7612357, 35.3184874],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_36045e52913644ec9ee7a246277dfa9a = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_7bb1aa5ee50e40b5a3fdfcb3dfe4b144.setIcon(custom_icon_36045e52913644ec9ee7a246277dfa9a);
        
    
            var marker_01679bdee94541f5a0e6a35048d6b5e7 = L.marker(
                [-24.4769532, 35.0306964],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_d5fcd07327ad4c3cb59506b810a0a14e = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_01679bdee94541f5a0e6a35048d6b5e7.setIcon(custom_icon_d5fcd07327ad4c3cb59506b810a0a14e);
        
    
            var marker_3f80b04bfea84f81b57ab700b08690dd = L.marker(
                [-23.8817275, 35.2292743],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_0c2247fb278f4323aa2827537ed69589 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_3f80b04bfea84f81b57ab700b08690dd.setIcon(custom_icon_0c2247fb278f4323aa2827537ed69589);
        
    
            var marker_1b781f2fa865495c87759ab8a24b7149 = L.marker(
                [-23.9226109, 35.1620116],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_2c4c183cfa25430195ea3a6082cdc857 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_1b781f2fa865495c87759ab8a24b7149.setIcon(custom_icon_2c4c183cfa25430195ea3a6082cdc857);
        
    
            var marker_67eeda52aaa9413b8d98dfffebbea8d4 = L.marker(
                [-23.9071447, 35.1940345],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_183b5e2ff7e648028c8bedad658f630e = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_67eeda52aaa9413b8d98dfffebbea8d4.setIcon(custom_icon_183b5e2ff7e648028c8bedad658f630e);
        
    
            var marker_ea9197eb84ea442fa63f617fdc0b6bef = L.marker(
                [-24.2762766, 33.0998342],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_6b8a2bf5c2cc45bf98d4b990117fd3c7 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_ea9197eb84ea442fa63f617fdc0b6bef.setIcon(custom_icon_6b8a2bf5c2cc45bf98d4b990117fd3c7);
        
    
            var marker_7f52b22ae5b54dfca5962265588e763d = L.marker(
                [-24.6625345, 33.3458696],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_2c4f8bf095f74a3b87b3b972da66e02b = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_7f52b22ae5b54dfca5962265588e763d.setIcon(custom_icon_2c4f8bf095f74a3b87b3b972da66e02b);
        
    
            var marker_02203b9804394e2a89f812511b0a4d2d = L.marker(
                [-24.5332533, 32.9973835],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_fec914f2f51448acb8910ec2e5977057 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_02203b9804394e2a89f812511b0a4d2d.setIcon(custom_icon_fec914f2f51448acb8910ec2e5977057);
        
    
            var marker_00d6db214c6840479a2c0ec88fb6af5e = L.marker(
                [-24.6311645, 34.0675483],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_90b4428717da4bc5864344669ac2458e = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_00d6db214c6840479a2c0ec88fb6af5e.setIcon(custom_icon_90b4428717da4bc5864344669ac2458e);
        
    
            var marker_fb671455ff7144b39f776af951f00229 = L.marker(
                [-24.5280039, 33.6752165],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_2ec570d187654c2a8417e326e24347c9 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_fb671455ff7144b39f776af951f00229.setIcon(custom_icon_2ec570d187654c2a8417e326e24347c9);
        
    
            var marker_41fbe304e2904f74b43bb9f3e17acf45 = L.marker(
                [-23.3848799, 32.3754286],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_8558f580e57445768ddaa3d0b5b3e091 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_41fbe304e2904f74b43bb9f3e17acf45.setIcon(custom_icon_8558f580e57445768ddaa3d0b5b3e091);
        
    
            var marker_8ff7015eedec4bba875bba80d62c41c5 = L.marker(
                [-19.1550794, 33.1468381],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_5691c137c89b48c38e7786c63b5c70e7 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_8ff7015eedec4bba875bba80d62c41c5.setIcon(custom_icon_5691c137c89b48c38e7786c63b5c70e7);
        
    
            var marker_72216861510041bc8cfe93d96336bb4e = L.marker(
                [-19.0315034, 32.916893],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_2281ef3623e34e108d4b42a37100597e = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_72216861510041bc8cfe93d96336bb4e.setIcon(custom_icon_2281ef3623e34e108d4b42a37100597e);
        
    
            var marker_6eb92d04b85c467783d6ac0faa7510c4 = L.marker(
                [-20.7344149, 32.5594416],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_72121e7fc1f84f3ead7a83145333c6e5 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_6eb92d04b85c467783d6ac0faa7510c4.setIcon(custom_icon_72121e7fc1f84f3ead7a83145333c6e5);
        
    
            var marker_08c364cd7d3644979125d5aebf1ef673 = L.marker(
                [-18.4580569, 33.6068282],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_7ceb42739d094a3bacbcee13bd72d648 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_08c364cd7d3644979125d5aebf1ef673.setIcon(custom_icon_7ceb42739d094a3bacbcee13bd72d648);
        
    
            var marker_0d63e8f1c02e4e2493df27f4f97accd4 = L.marker(
                [-20.6704438, 33.5334688],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_3bc38968b386415b8e361e2ce3505a28 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_0d63e8f1c02e4e2493df27f4f97accd4.setIcon(custom_icon_3bc38968b386415b8e361e2ce3505a28);
        
    
            var marker_43738a04c83948d99bab00984037412d = L.marker(
                [-20.8243999, 33.3697014],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_cadbc8976c314732b15b8b1d7f4dae15 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_43738a04c83948d99bab00984037412d.setIcon(custom_icon_cadbc8976c314732b15b8b1d7f4dae15);
        
    
            var marker_05258362635a4c14a61377b0b408a5ab = L.marker(
                [-19.0521895, 33.7852697],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_40beae4faf7c4c3abdc0f14c4cc1496e = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_05258362635a4c14a61377b0b408a5ab.setIcon(custom_icon_40beae4faf7c4c3abdc0f14c4cc1496e);
        
    
            var marker_dbbbf4eea7954c7cbe36191295241277 = L.marker(
                [-16.6038523, 39.2506213],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_c916374e6853402286712707b8a73407 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_dbbbf4eea7954c7cbe36191295241277.setIcon(custom_icon_c916374e6853402286712707b8a73407);
        
    
            var marker_47da4071b11c4f35a23c600818b3e73f = L.marker(
                [-17.9476448, 33.1939097],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_0c261176c56e4fa1afa09f1128809248 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_47da4071b11c4f35a23c600818b3e73f.setIcon(custom_icon_0c261176c56e4fa1afa09f1128809248);
        
    
            var marker_438c92e637c04e8989321aaf3a22131b = L.marker(
                [-19.2026742, 33.9258496],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_b71b65fed70544388e6f2b26814cfe9d = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_438c92e637c04e8989321aaf3a22131b.setIcon(custom_icon_b71b65fed70544388e6f2b26814cfe9d);
        
    
            var marker_dfad493bfd7e4efda4155c439f9fb24b = L.marker(
                [-19.0723823, 33.364006],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_7e5a758d170841508b1c15c7705310c9 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_dfad493bfd7e4efda4155c439f9fb24b.setIcon(custom_icon_7e5a758d170841508b1c15c7705310c9);
        
    
            var marker_c626354b666a4fdbbfd195cc1e895522 = L.marker(
                [-17.41998, 33.3488917],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_25cb0bb3607b4ec3a3d222349f02ff5d = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_c626354b666a4fdbbfd195cc1e895522.setIcon(custom_icon_25cb0bb3607b4ec3a3d222349f02ff5d);
        
    
            var marker_2944fc142b0c41bb990bff41de475a88 = L.marker(
                [-19.1089001, 32.9281006],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_3c522437844e4b3fb8468afe2b1e5dd3 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_2944fc142b0c41bb990bff41de475a88.setIcon(custom_icon_3c522437844e4b3fb8468afe2b1e5dd3);
        
    
            var marker_ffe081b515f94357bd9c8aee08079445 = L.marker(
                [-15.3862379, 37.7677553],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_3623ef7857e440fc95621345705fd5b3 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_ffe081b515f94357bd9c8aee08079445.setIcon(custom_icon_3623ef7857e440fc95621345705fd5b3);
        
    
            var marker_42cba05a599c4d5a99660ca7a6035fba = L.marker(
                [-17.7470875, 36.9277391],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_c2778536f4e3452c858449302f972d50 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_42cba05a599c4d5a99660ca7a6035fba.setIcon(custom_icon_c2778536f4e3452c858449302f972d50);
        
    
            var marker_68f800f596d8453b941948598037cc94 = L.marker(
                [-16.4072449, 39.0363133],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_48eda2a1e0714282b92f1c47197f3b17 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_68f800f596d8453b941948598037cc94.setIcon(custom_icon_48eda2a1e0714282b92f1c47197f3b17);
        
    
            var marker_c94174a58e2e4a80be12398909aa5f35 = L.marker(
                [-19.0832087, 33.6454586],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_781e878173ae4ea28447d4ced0222bff = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_c94174a58e2e4a80be12398909aa5f35.setIcon(custom_icon_781e878173ae4ea28447d4ced0222bff);
        
    
            var marker_ce568b4a888547e9930714f6b4310be3 = L.marker(
                [-19.4149753, 33.5130112],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_341791a060704c379775e39e4e914cf7 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_ce568b4a888547e9930714f6b4310be3.setIcon(custom_icon_341791a060704c379775e39e4e914cf7);
        
    
            var marker_4f6ad799c854429486f0df11efd60bbd = L.marker(
                [-17.900171, 33.9391934],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_b1e0872884ed4494b4110b7ad30f067d = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_4f6ad799c854429486f0df11efd60bbd.setIcon(custom_icon_b1e0872884ed4494b4110b7ad30f067d);
        
    
            var marker_984ceea429354125b01b74104ea81574 = L.marker(
                [-21.2905586, 33.4596787],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_c88b8fb2e6c94e55bff0700cd7069e4a = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_984ceea429354125b01b74104ea81574.setIcon(custom_icon_c88b8fb2e6c94e55bff0700cd7069e4a);
        
    
            var marker_be4a837ec9c04ac08650ea88efd5f2a9 = L.marker(
                [-21.3704751, 32.6277464],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_f7e64055c34f46dea41f0e06e0e4ee8c = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_be4a837ec9c04ac08650ea88efd5f2a9.setIcon(custom_icon_f7e64055c34f46dea41f0e06e0e4ee8c);
        
    
            var marker_d4eb30b55da14f40922ead9f056a86b1 = L.marker(
                [-19.267448, 33.4803492],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_2316910a70c845dfb5f8901a8095717e = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_d4eb30b55da14f40922ead9f056a86b1.setIcon(custom_icon_2316910a70c845dfb5f8901a8095717e);
        
    
            var marker_fe87d2703d3c46cd8b1846967b6060ca = L.marker(
                [-18.9994753, 33.3874337],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_49f4f7a84d9d4bb7ac6b588d2e06907e = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_fe87d2703d3c46cd8b1846967b6060ca.setIcon(custom_icon_49f4f7a84d9d4bb7ac6b588d2e06907e);
        
    
            var marker_bee2979f12fa48a5bdc60edbd1d2639f = L.marker(
                [-18.9957088, 32.7267803],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_7a02e601e7484b529d4a070887efab3d = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_bee2979f12fa48a5bdc60edbd1d2639f.setIcon(custom_icon_7a02e601e7484b529d4a070887efab3d);
        
    
            var marker_efc664808af54bce858e5d28bb5982e6 = L.marker(
                [-20.8625288, 32.583113],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_338d4b6274cc438b9833fc6c86a6f6fc = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_efc664808af54bce858e5d28bb5982e6.setIcon(custom_icon_338d4b6274cc438b9833fc6c86a6f6fc);
        
    
            var marker_bcc761a292e54cbb86df16f91fe774f6 = L.marker(
                [-13.8450934, 39.54354],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_04c39cacb4434b44a78d573b03119c6b = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_bcc761a292e54cbb86df16f91fe774f6.setIcon(custom_icon_04c39cacb4434b44a78d573b03119c6b);
        
    
            var marker_f49fbdc7edd54466a3a11b43173bec75 = L.marker(
                [-20.5778218, 32.7732387],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_6d7c97aedc8d46538db9f29df609007b = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_f49fbdc7edd54466a3a11b43173bec75.setIcon(custom_icon_6d7c97aedc8d46538db9f29df609007b);
        
    
            var marker_baf2d37821c741ff94c880465e77a2cd = L.marker(
                [-25.2248663, 32.6646052],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_dbddb2ec05754e91a8a404b5b4a46c11 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_baf2d37821c741ff94c880465e77a2cd.setIcon(custom_icon_dbddb2ec05754e91a8a404b5b4a46c11);
        
    
            var marker_74ac673e372e440a9dab78d7ba2ccbf0 = L.marker(
                [-17.5822419, 34.309304],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_10471357b68847fc9c39c479edb59989 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_74ac673e372e440a9dab78d7ba2ccbf0.setIcon(custom_icon_10471357b68847fc9c39c479edb59989);
        
    
            var marker_8ad1bcedd10b4af48f27af49c99351d3 = L.marker(
                [-14.9206429, 40.2986254],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_33e0b3bd1dfc4023821830b20134e730 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_8ad1bcedd10b4af48f27af49c99351d3.setIcon(custom_icon_33e0b3bd1dfc4023821830b20134e730);
        
    
            var marker_28377aff98124afb8e8ea156da71b237 = L.marker(
                [-15.5650771, 37.790569],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_9a584158d3c246abbcaa379c719e5614 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_28377aff98124afb8e8ea156da71b237.setIcon(custom_icon_9a584158d3c246abbcaa379c719e5614);
        
    
            var marker_7de18f51bce54a228caccb702a1ec61d = L.marker(
                [-14.9523778, 40.6657541],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_bb268044924a44768d5527d878c5bc25 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_7de18f51bce54a228caccb702a1ec61d.setIcon(custom_icon_bb268044924a44768d5527d878c5bc25);
        
    
            var marker_5b1875f8d13f46ceada5dbee341969b3 = L.marker(
                [-15.5848096, 38.4184439],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_d7700f24f1634c389fd600089c5c7e59 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_5b1875f8d13f46ceada5dbee341969b3.setIcon(custom_icon_d7700f24f1634c389fd600089c5c7e59);
        
    
            var marker_e0b91b05791847aa8ec4e834c8e8321e = L.marker(
                [-25.4952554, 32.078324],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a6200d5a4121421e88766aa0cb9b59e7 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_e0b91b05791847aa8ec4e834c8e8321e.setIcon(custom_icon_a6200d5a4121421e88766aa0cb9b59e7);
        
    
            var marker_f458926dbcd74dbb9d33835fb985cec2 = L.marker(
                [-25.6641053, 32.6423804],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ba6637f930784b23956ef43e7fc27e35 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_f458926dbcd74dbb9d33835fb985cec2.setIcon(custom_icon_ba6637f930784b23956ef43e7fc27e35);
        
    
            var marker_15ff64c305e44579afe88c2895b1027b = L.marker(
                [-25.0936818, 32.9175161],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_3b2bf6625976444dae06f46d74a6a74c = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_15ff64c305e44579afe88c2895b1027b.setIcon(custom_icon_3b2bf6625976444dae06f46d74a6a74c);
        
    
            var marker_acf46c6752414b38b481c192dc792c0a = L.marker(
                [-25.696037, 32.3448913],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_88d4eb89f0444a7c95965fca9796600f = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_acf46c6752414b38b481c192dc792c0a.setIcon(custom_icon_88d4eb89f0444a7c95965fca9796600f);
        
    
            var marker_a621543ff9e04b56b370eca7c9044b03 = L.marker(
                [-24.5693355, 32.6619525],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_3b540b83eae54f0ca879135b458c7f1f = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_a621543ff9e04b56b370eca7c9044b03.setIcon(custom_icon_3b540b83eae54f0ca879135b458c7f1f);
        
    
            var marker_46fdc9185d78418d93d606ff0aba9fd8 = L.marker(
                [-25.7509316, 32.3947629],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_b420a6c5a8a94370aa82a0c5f2e2ca44 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_46fdc9185d78418d93d606ff0aba9fd8.setIcon(custom_icon_b420a6c5a8a94370aa82a0c5f2e2ca44);
        
    
            var marker_f46e25f11aa14a20beabc80e2ff85836 = L.marker(
                [-26.6719818, 32.1822247],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ff23977c559d4598853fd49630501db8 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_f46e25f11aa14a20beabc80e2ff85836.setIcon(custom_icon_ff23977c559d4598853fd49630501db8);
        
    
            var marker_611af379312644ab82b0347d81806c85 = L.marker(
                [-26.7508822, 32.8261735],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a0b6b6ea89204342883f1d09ddc8eb11 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_611af379312644ab82b0347d81806c85.setIcon(custom_icon_a0b6b6ea89204342883f1d09ddc8eb11);
        
    
            var marker_a2578c33393c4909ab0bda93422ed4b7 = L.marker(
                [-26.8400373, 32.2859189],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_bf1e2d7a3e9449689ee9b555dde93271 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_a2578c33393c4909ab0bda93422ed4b7.setIcon(custom_icon_bf1e2d7a3e9449689ee9b555dde93271);
        
    
            var marker_3da9c04d61814f7784f1b8c01c38cdc6 = L.marker(
                [-26.0081522, 32.3367421],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_93bb3c967fce436eb95946833046cd6b = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_3da9c04d61814f7784f1b8c01c38cdc6.setIcon(custom_icon_93bb3c967fce436eb95946833046cd6b);
        
    
            var marker_58e4d77d84b94fbda36d031b33bfadbf = L.marker(
                [-25.1573829, 32.8005557],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ebc9cf03f59a400aa38f47fc652297be = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_58e4d77d84b94fbda36d031b33bfadbf.setIcon(custom_icon_ebc9cf03f59a400aa38f47fc652297be);
        
    
            var marker_6abcc3300e27401dbc262f0169787157 = L.marker(
                [-26.3287803, 32.4156734],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_d7e4d965e3d840a7b25641e81218be54 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_6abcc3300e27401dbc262f0169787157.setIcon(custom_icon_d7e4d965e3d840a7b25641e81218be54);
        
    
            var marker_e438f22e6e9042b08ec557a7e9551805 = L.marker(
                [-25.9185865, 32.39426],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_eee7fb008b3c4120af5410a1a3468ec9 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_e438f22e6e9042b08ec557a7e9551805.setIcon(custom_icon_eee7fb008b3c4120af5410a1a3468ec9);
        
    
            var marker_43562530f43f47d3935f01a49ce37044 = L.marker(
                [-24.9007608, 32.3492016],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_6d23ada77d00481aa81fc70642fca374 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_43562530f43f47d3935f01a49ce37044.setIcon(custom_icon_6d23ada77d00481aa81fc70642fca374);
        
    
            var marker_407e11a5b86a4c7d941c901576432e6c = L.marker(
                [-25.8642704, 32.2850284],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_e7cee646811744c390c381213b3040e3 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_407e11a5b86a4c7d941c901576432e6c.setIcon(custom_icon_e7cee646811744c390c381213b3040e3);
        
    
            var marker_f22135f7e66c4670ab415a8e9ae6aaa0 = L.marker(
                [-14.3709613, 38.8067472],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_2a912eafcd9045d1b8a63dcb07a3217f = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_f22135f7e66c4670ab415a8e9ae6aaa0.setIcon(custom_icon_2a912eafcd9045d1b8a63dcb07a3217f);
        
    
            var marker_8af70d0eff374275bdce36a1883dd061 = L.marker(
                [-25.9910394, 32.0132817],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a833147ff0c64fc2b57e5c15fff7758f = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_8af70d0eff374275bdce36a1883dd061.setIcon(custom_icon_a833147ff0c64fc2b57e5c15fff7758f);
        
    
            var marker_43d9209f59144c08b051e2ad8adf9803 = L.marker(
                [-15.0286528, 37.5140575],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_c52f34a97c104fb2b4579b5c8370c117 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_43d9209f59144c08b051e2ad8adf9803.setIcon(custom_icon_c52f34a97c104fb2b4579b5c8370c117);
        
    
            var marker_b1df44129df34e95b0eca5b087ddfde7 = L.marker(
                [-14.9931054, 38.269541],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_f66b889e5bc74d3e81f86ddfe1a8b12a = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_b1df44129df34e95b0eca5b087ddfde7.setIcon(custom_icon_f66b889e5bc74d3e81f86ddfe1a8b12a);
        
    
            var marker_fc060d620920408098b2f4f6de529dbe = L.marker(
                [-14.9688555, 39.8855545],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_fe4945a282b640739ca68e53de4e9389 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_fc060d620920408098b2f4f6de529dbe.setIcon(custom_icon_fe4945a282b640739ca68e53de4e9389);
        
    
            var marker_f8c0662d14514a428a1ef908e1434b6e = L.marker(
                [-15.7193668, 39.6936746],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_cd8c74b6f5c94dddae7aa1c831ab52b7 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_f8c0662d14514a428a1ef908e1434b6e.setIcon(custom_icon_cd8c74b6f5c94dddae7aa1c831ab52b7);
        
    
            var marker_c10595d6134f4e8aba37f9d2338d42c8 = L.marker(
                [-16.7112743, 39.3189816],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_0a7ed0c2a0e04d09849363a9fc7a245e = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_c10595d6134f4e8aba37f9d2338d42c8.setIcon(custom_icon_0a7ed0c2a0e04d09849363a9fc7a245e);
        
    
            var marker_956047de253344debd6d012df851f471 = L.marker(
                [-14.5816577, 39.7407655],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_d45e80491dde416896929f7962413e6e = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_956047de253344debd6d012df851f471.setIcon(custom_icon_d45e80491dde416896929f7962413e6e);
        
    
            var marker_92281c99f0f84e52bdcf775e8c3c0a28 = L.marker(
                [-16.8501249, 36.9833953],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_6e86d01db22f4d319945bd2cab731db4 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_92281c99f0f84e52bdcf775e8c3c0a28.setIcon(custom_icon_6e86d01db22f4d319945bd2cab731db4);
        
    
            var marker_464a8f0e161e4794a9b1b81d52c601f3 = L.marker(
                [-25.4436749, 31.9894643],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_b5f84db9cdea434d88dfe9d89203cfff = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_464a8f0e161e4794a9b1b81d52c601f3.setIcon(custom_icon_b5f84db9cdea434d88dfe9d89203cfff);
        
    
            var marker_881ee20e35fa419f8ec6b9bfa8689f82 = L.marker(
                [-25.2392164, 32.1375692],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_2743d011a8b743329808e67fb6bc1050 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_881ee20e35fa419f8ec6b9bfa8689f82.setIcon(custom_icon_2743d011a8b743329808e67fb6bc1050);
        
    
            var marker_93e9d3196fbb472c8b49db00e91289e9 = L.marker(
                [-25.7847499, 32.6340821],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_8e285761c57f461eadf9aa23157987e3 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_93e9d3196fbb472c8b49db00e91289e9.setIcon(custom_icon_8e285761c57f461eadf9aa23157987e3);
        
    
            var marker_5995d5c51e3348508cc97c700a72b891 = L.marker(
                [-26.4745007, 32.6511002],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_64249f69c06940478920f4fb84b6ccd2 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_5995d5c51e3348508cc97c700a72b891.setIcon(custom_icon_64249f69c06940478920f4fb84b6ccd2);
        
    
            var marker_0b98a8b942054be7bad675898b4a56e8 = L.marker(
                [-25.3217188, 32.2553445],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_5740c505b8864a0eb5155a23fc7bdef2 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_0b98a8b942054be7bad675898b4a56e8.setIcon(custom_icon_5740c505b8864a0eb5155a23fc7bdef2);
        
    
            var marker_42c4e3d0dbfd4250a6b9688a257b1437 = L.marker(
                [-25.2623571, 32.8646366],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_1ee7e4a9a700446886d44336718a9bb8 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_42c4e3d0dbfd4250a6b9688a257b1437.setIcon(custom_icon_1ee7e4a9a700446886d44336718a9bb8);
        
    
            var marker_c3326c0dafa3469bbbc498955fde7d3f = L.marker(
                [-19.4129819, 33.2952711],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_6927825f240347fe8683211cf8cde0e2 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_c3326c0dafa3469bbbc498955fde7d3f.setIcon(custom_icon_6927825f240347fe8683211cf8cde0e2);
        
    
            var marker_feec68cf2f2448b9b114cd27b4deadff = L.marker(
                [-21.3179401, 33.282835],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_322cac32eac34356867ec6858b825b96 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_feec68cf2f2448b9b114cd27b4deadff.setIcon(custom_icon_322cac32eac34356867ec6858b825b96);
        
    
            var marker_a9ebe5020ab949fea4e27f6088fca0e4 = L.marker(
                [-21.4494724, 33.0839065],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_90c002340df645149ae9853654fba22f = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_a9ebe5020ab949fea4e27f6088fca0e4.setIcon(custom_icon_90c002340df645149ae9853654fba22f);
        
    
            var marker_4f5ba76ba47640338805877f553305e3 = L.marker(
                [-16.8218288, 34.4474567],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_46f3289b82034e0d8b1a3c8dc3da1594 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_4f5ba76ba47640338805877f553305e3.setIcon(custom_icon_46f3289b82034e0d8b1a3c8dc3da1594);
        
    
            var marker_1da08b1d52844cb8a5a0ab8333668125 = L.marker(
                [-19.544247, 32.8946541],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ac13670336d14bed9fd8d299320e324d = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_1da08b1d52844cb8a5a0ab8333668125.setIcon(custom_icon_ac13670336d14bed9fd8d299320e324d);
        
    
            var marker_d751a66c7ce04702a428417b8f1a227c = L.marker(
                [-18.5561974, 33.2794137],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_79087d93ad1a4b39907990d1b3f61c9d = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_d751a66c7ce04702a428417b8f1a227c.setIcon(custom_icon_79087d93ad1a4b39907990d1b3f61c9d);
        
    
            var marker_c89bbc68965e460a8a10271a8cb49ba2 = L.marker(
                [-18.330533, 33.1155691],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_abb59c48926e435f9288db6666fc8e63 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_c89bbc68965e460a8a10271a8cb49ba2.setIcon(custom_icon_abb59c48926e435f9288db6666fc8e63);
        
    
            var marker_39d535b0a6904c248571f8d458835356 = L.marker(
                [-17.6034132, 33.2540899],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ba852f177c054b7f9e01d55406ff7be0 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_39d535b0a6904c248571f8d458835356.setIcon(custom_icon_ba852f177c054b7f9e01d55406ff7be0);
        
    
            var marker_a8d521f274364806a7a1e4d869910d82 = L.marker(
                [-17.7974298, 33.2192166],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a403103a6efe46bf911da14ee071da7e = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_a8d521f274364806a7a1e4d869910d82.setIcon(custom_icon_a403103a6efe46bf911da14ee071da7e);
        
    
            var marker_db5a7138c87e4a3b90597a4316c6c551 = L.marker(
                [-19.313374, 33.2481994],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_13d0d8bab7384f8c97222f754c6c747f = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_db5a7138c87e4a3b90597a4316c6c551.setIcon(custom_icon_13d0d8bab7384f8c97222f754c6c747f);
        
    
            var marker_3358694266dc4595a8c076418d158f65 = L.marker(
                [-18.863207, 32.8260451],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_b49f3d576cf542d58a8bdc0c11df39d4 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_3358694266dc4595a8c076418d158f65.setIcon(custom_icon_b49f3d576cf542d58a8bdc0c11df39d4);
        
    
            var marker_73b3302835334ec684924d8e5e45d632 = L.marker(
                [-16.7896527, 33.5417457],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_dcb81468e40647ed8ef3accfa6d48053 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_73b3302835334ec684924d8e5e45d632.setIcon(custom_icon_dcb81468e40647ed8ef3accfa6d48053);
        
    
            var marker_7817eb8052db4922bc2ff8cc850ed6af = L.marker(
                [-17.8409155, 33.4549119],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_cd42089e05fd42b8b8e58801d061c6aa = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_7817eb8052db4922bc2ff8cc850ed6af.setIcon(custom_icon_cd42089e05fd42b8b8e58801d061c6aa);
        
    
            var marker_036c1ee28b3740acba8e0a901c3b2be0 = L.marker(
                [-16.870302, 34.0763294],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_048ec2d452d0415daab8536ac8b7c699 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_036c1ee28b3740acba8e0a901c3b2be0.setIcon(custom_icon_048ec2d452d0415daab8536ac8b7c699);
        
    
            var marker_952cbaa8c0024cd697c12f78006b362d = L.marker(
                [-19.1511513, 33.6609731],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_58814546f4674dd7bcef8b07286ba636 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_952cbaa8c0024cd697c12f78006b362d.setIcon(custom_icon_58814546f4674dd7bcef8b07286ba636);
        
    
            var marker_1431809173f2492ea28fcb2950969c20 = L.marker(
                [-17.9950833, 33.2258289],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_98902f2193874feb9652735c7c062c3d = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_1431809173f2492ea28fcb2950969c20.setIcon(custom_icon_98902f2193874feb9652735c7c062c3d);
        
    
            var marker_6fcb6343b6dd4148ac74ebcb02a0d72e = L.marker(
                [-17.7083896, 33.9714762],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ff10d9eea5ae4c3ca36381edc85d1d26 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_6fcb6343b6dd4148ac74ebcb02a0d72e.setIcon(custom_icon_ff10d9eea5ae4c3ca36381edc85d1d26);
        
    
            var marker_9369df3898ca482fa03dca502ee3bf2b = L.marker(
                [-20.247843, 32.9109424],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_8af406c1feac490abc12e74824b60900 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_9369df3898ca482fa03dca502ee3bf2b.setIcon(custom_icon_8af406c1feac490abc12e74824b60900);
        
    
            var marker_1765c78d5c244e77b68750a8b6487f47 = L.marker(
                [-19.4889161, 33.2855981],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_58f8eba3d0404fea88d9b64d7e12da99 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_1765c78d5c244e77b68750a8b6487f47.setIcon(custom_icon_58f8eba3d0404fea88d9b64d7e12da99);
        
    
            var marker_5062da35c65a405dbbf48f311e946d27 = L.marker(
                [-17.1664867, 33.5543397],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_029310365c5b447f9973cf773f5aaf22 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_5062da35c65a405dbbf48f311e946d27.setIcon(custom_icon_029310365c5b447f9973cf773f5aaf22);
        
    
            var marker_45e74a029bee4c109bef9f79066664be = L.marker(
                [-18.963701, 32.7722932],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_390b902d555e4778a71b27d6cebdbe05 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_45e74a029bee4c109bef9f79066664be.setIcon(custom_icon_390b902d555e4778a71b27d6cebdbe05);
        
    
            var marker_baebc9b350fb40118201417b47e2205c = L.marker(
                [-18.9293773, 32.797882],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_fc1cc8ea19f848aaa70d18be185a5d02 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_baebc9b350fb40118201417b47e2205c.setIcon(custom_icon_fc1cc8ea19f848aaa70d18be185a5d02);
        
    
            var marker_f5cc0ef0413b4e94a7ab5d3863275ea0 = L.marker(
                [-20.567157, 32.6815703],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_23598312ead545c48747a1a274353541 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_f5cc0ef0413b4e94a7ab5d3863275ea0.setIcon(custom_icon_23598312ead545c48747a1a274353541);
        
    
            var marker_fce7ea7b0002420abde5e1daa717208a = L.marker(
                [-19.3285105, 33.8337701],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_eede79b190464937989c07924eac0af0 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_fce7ea7b0002420abde5e1daa717208a.setIcon(custom_icon_eede79b190464937989c07924eac0af0);
        
    
            var marker_9a82e5c2dc5e4e6eaa6e63c692fe170a = L.marker(
                [-18.9866289, 33.0814143],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_0a51e7686792489a99cb4ab30418e60f = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_9a82e5c2dc5e4e6eaa6e63c692fe170a.setIcon(custom_icon_0a51e7686792489a99cb4ab30418e60f);
        
    
            var marker_be54375c411d479cb8232010d6737756 = L.marker(
                [-19.5453721, 33.5090217],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_6056d47d27db451a8c813f269ffab0e0 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_be54375c411d479cb8232010d6737756.setIcon(custom_icon_6056d47d27db451a8c813f269ffab0e0);
        
    
            var marker_812c73b6527c4b109a855c6fc1ad1374 = L.marker(
                [-18.6243179, 33.0394808],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_796376349f534ce5b2d4fc23c77dfe42 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_812c73b6527c4b109a855c6fc1ad1374.setIcon(custom_icon_796376349f534ce5b2d4fc23c77dfe42);
        
    
            var marker_fe50848d3e994f5e9186646b6a1ecf68 = L.marker(
                [-25.8001295, 32.6419561],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_8c2dc67c7a3149fbab0da6aa9c5bdef4 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_fe50848d3e994f5e9186646b6a1ecf68.setIcon(custom_icon_8c2dc67c7a3149fbab0da6aa9c5bdef4);
        
    
            var marker_a5dbcb0cfb5f43ccaf109734afc87e8b = L.marker(
                [-26.0490633, 32.3255799],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_6fe71715a305438fb1a8ef58a5b70fa1 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_a5dbcb0cfb5f43ccaf109734afc87e8b.setIcon(custom_icon_6fe71715a305438fb1a8ef58a5b70fa1);
        
    
            var marker_f44ac8d71e0845a38e523f46954d78b2 = L.marker(
                [-25.2872555, 32.7409265],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_9fb6cc096ce04305b617c4b6de55e64d = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_f44ac8d71e0845a38e523f46954d78b2.setIcon(custom_icon_9fb6cc096ce04305b617c4b6de55e64d);
        
    
            var marker_936ad3536074422e81cd2b3c10c33e36 = L.marker(
                [-14.8855, 37.7723007],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_8a530ee20bfc4964ae7d2c198938d815 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_936ad3536074422e81cd2b3c10c33e36.setIcon(custom_icon_8a530ee20bfc4964ae7d2c198938d815);
        
    
            var marker_572ee1b842f4438d90087a147fa2f2a5 = L.marker(
                [-15.4566093, 36.955398],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_f1e23e03491b48d99ac8b65461aae8fb = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_572ee1b842f4438d90087a147fa2f2a5.setIcon(custom_icon_f1e23e03491b48d99ac8b65461aae8fb);
        
    
            var marker_611b3b05c9ea4cbbb3e881e75679445a = L.marker(
                [-14.3002171, 39.7505428],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_c2f3586065e14c228f57774f1d05b238 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_611b3b05c9ea4cbbb3e881e75679445a.setIcon(custom_icon_c2f3586065e14c228f57774f1d05b238);
        
    
            var marker_eceeb977254649288078ad6c9117166f = L.marker(
                [-25.8408652, 32.3637673],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_d6119fbf9813425f880e84fa6d20671b = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_eceeb977254649288078ad6c9117166f.setIcon(custom_icon_d6119fbf9813425f880e84fa6d20671b);
        
    
            var marker_1792a1bf674c4bbcb371c6ff96778c68 = L.marker(
                [-26.0856281, 32.6239564],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_8b2446ca9f634a5d999799dc881cfb46 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_1792a1bf674c4bbcb371c6ff96778c68.setIcon(custom_icon_8b2446ca9f634a5d999799dc881cfb46);
        
    
            var marker_fbc17d4c0791492b9ce139317e8fc2f9 = L.marker(
                [-24.8864002, 32.5285988],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_cd340949e8254176849e2665ce85ec4c = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_fbc17d4c0791492b9ce139317e8fc2f9.setIcon(custom_icon_cd340949e8254176849e2665ce85ec4c);
        
    
            var marker_2425bdba785a42f895dbc4edb504f3b7 = L.marker(
                [-26.1917009, 32.9337716],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_e2f1f60d6fec4a77bf74b812d77b3b76 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_2425bdba785a42f895dbc4edb504f3b7.setIcon(custom_icon_e2f1f60d6fec4a77bf74b812d77b3b76);
        
    
            var marker_a9b03061bc4146c5911822b57bb2c2dd = L.marker(
                [-14.9168106, 40.3019634],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_bfea024897fb48208f6bfc07e0d6a525 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_a9b03061bc4146c5911822b57bb2c2dd.setIcon(custom_icon_bfea024897fb48208f6bfc07e0d6a525);
        
    
            var marker_21fe6e53d0314cff9fe53fb44e752e3c = L.marker(
                [-17.1171321, 38.1296857],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_2ddd808a435b45f3a2369f4c6b46fa3e = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_21fe6e53d0314cff9fe53fb44e752e3c.setIcon(custom_icon_2ddd808a435b45f3a2369f4c6b46fa3e);
        
    
            var marker_d447eee938734a57a31fc914d88c1dec = L.marker(
                [-15.6236214, 39.1018526],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_abea7b24435b494bbf7bdcebefede851 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_d447eee938734a57a31fc914d88c1dec.setIcon(custom_icon_abea7b24435b494bbf7bdcebefede851);
        
    
            var marker_148a0d5eb26a43668c8f25cef204d651 = L.marker(
                [-14.9422737, 39.4155523],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_2893a178fe1445bead9beb2fb1461405 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_148a0d5eb26a43668c8f25cef204d651.setIcon(custom_icon_2893a178fe1445bead9beb2fb1461405);
        
    
            var marker_d76a31bbe26148a48663566fe27e463e = L.marker(
                [-16.281004, 37.3213943],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_042b43058b0e4eada6be5daec8f4dbd1 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_d76a31bbe26148a48663566fe27e463e.setIcon(custom_icon_042b43058b0e4eada6be5daec8f4dbd1);
        
    
            var marker_2efac89fda7346a09404c5ecad2dd66b = L.marker(
                [-17.451076, 35.0787105],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_186d517759d348498a26eb2dcb3e3237 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_2efac89fda7346a09404c5ecad2dd66b.setIcon(custom_icon_186d517759d348498a26eb2dcb3e3237);
        
    
            var marker_c2f3167f040944839b382256addb9611 = L.marker(
                [-25.5987396, 32.2449642],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_5e1bb17e150b424ebee092a3ebe730c6 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_c2f3167f040944839b382256addb9611.setIcon(custom_icon_5e1bb17e150b424ebee092a3ebe730c6);
        
    
            var marker_4d77495fcff14e48afdf60dafa6c2d52 = L.marker(
                [-15.1383996, 39.0358076],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_3e5232a278b04972acf108dbe0793011 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_4d77495fcff14e48afdf60dafa6c2d52.setIcon(custom_icon_3e5232a278b04972acf108dbe0793011);
        
    
            var marker_25be695ac3c94d3db77b9abf4c5e5ce4 = L.marker(
                [-25.761462, 32.5686061],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_5d7b92b394474de3be2ef4356716dacc = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_25be695ac3c94d3db77b9abf4c5e5ce4.setIcon(custom_icon_5d7b92b394474de3be2ef4356716dacc);
        
    
            var marker_733882c7580d47f7b5b79b782732a5aa = L.marker(
                [-26.0395337, 32.323081],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_d247fc8ab83c4a00b88c5e157c87b4a1 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_733882c7580d47f7b5b79b782732a5aa.setIcon(custom_icon_d247fc8ab83c4a00b88c5e157c87b4a1);
        
    
            var marker_6f5cbcd2e2f94d44952a012c319c0b4a = L.marker(
                [-26.2156087, 32.8857243],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_e0d117c2a4904fe48610b7b0b4d7f9fb = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_6f5cbcd2e2f94d44952a012c319c0b4a.setIcon(custom_icon_e0d117c2a4904fe48610b7b0b4d7f9fb);
        
    
            var marker_0eda939e72814e689cbbe1cd407e4acd = L.marker(
                [-26.064394, 32.2866318],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_197be8dfd3884013a5805dde375dcab6 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_0eda939e72814e689cbbe1cd407e4acd.setIcon(custom_icon_197be8dfd3884013a5805dde375dcab6);
        
    
            var marker_d1263a8bdac348208dc5c28e003969bc = L.marker(
                [-25.0456884, 32.8035422],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_b932e298a3904e3b9bf55db7269be97d = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_d1263a8bdac348208dc5c28e003969bc.setIcon(custom_icon_b932e298a3904e3b9bf55db7269be97d);
        
    
            var marker_d268a5a4db1e402086d62c844890e90f = L.marker(
                [-25.7495158, 32.6097401],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_e179ad3a5f7b4b11ac7779e3396e7a83 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_d268a5a4db1e402086d62c844890e90f.setIcon(custom_icon_e179ad3a5f7b4b11ac7779e3396e7a83);
        
    
            var marker_4bbc56dab49e4103b733c7dba57f5496 = L.marker(
                [-26.0424133, 32.3303668],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_585e10a4098c45a095bc0ac4f91aa1cb = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_4bbc56dab49e4103b733c7dba57f5496.setIcon(custom_icon_585e10a4098c45a095bc0ac4f91aa1cb);
        
    
            var marker_1a8b65b7c1ca4f3ca7eb6b6911f75c78 = L.marker(
                [-25.9623132, 32.4587837],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_156172fddba046b98117f704a24628f5 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_1a8b65b7c1ca4f3ca7eb6b6911f75c78.setIcon(custom_icon_156172fddba046b98117f704a24628f5);
        
    
            var marker_9a63b764d57a45a39700fa3e0b82ad16 = L.marker(
                [-14.9994556, 39.3445851],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_b98b44fb65c94a289502f6d6ae40d3dd = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_9a63b764d57a45a39700fa3e0b82ad16.setIcon(custom_icon_b98b44fb65c94a289502f6d6ae40d3dd);
        
    
            var marker_7ebc0b5df00a4236891ca3cd1b899f5a = L.marker(
                [-16.0751534, 39.6185862],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_6e204013df6a4247bfeccd2f602cce11 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_7ebc0b5df00a4236891ca3cd1b899f5a.setIcon(custom_icon_6e204013df6a4247bfeccd2f602cce11);
        
    
            var marker_11463787d02745f4ac08a2093a850f5e = L.marker(
                [-15.375347, 39.0347551],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ab56b429113443e08690414216e62e56 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_11463787d02745f4ac08a2093a850f5e.setIcon(custom_icon_ab56b429113443e08690414216e62e56);
        
    
            var marker_52b1ade0370f4fe58fd5239c3540567a = L.marker(
                [-15.4208529, 38.7920742],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_5a7a5633f4b341658f2cf527c303a5d2 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_52b1ade0370f4fe58fd5239c3540567a.setIcon(custom_icon_5a7a5633f4b341658f2cf527c303a5d2);
        
    
            var marker_043dac0bf20643efb134de95ffb92b39 = L.marker(
                [-14.5803309, 39.3780544],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a03f8222ab4c4666aa0b91f9ac1de147 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_043dac0bf20643efb134de95ffb92b39.setIcon(custom_icon_a03f8222ab4c4666aa0b91f9ac1de147);
        
    
            var marker_6fc6fc49fcdc4331bff6cef2d3add6cc = L.marker(
                [-15.3454728, 38.8910562],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_458523a54f0a4e29b6dd4adb9fb59580 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_6fc6fc49fcdc4331bff6cef2d3add6cc.setIcon(custom_icon_458523a54f0a4e29b6dd4adb9fb59580);
        
    
            var marker_4cac2fd1810d48e684c0deec06fa44ff = L.marker(
                [-25.5105178, 32.7264047],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_1d805bc48325465382c3aaffa696fc2f = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_4cac2fd1810d48e684c0deec06fa44ff.setIcon(custom_icon_1d805bc48325465382c3aaffa696fc2f);
        
    
            var marker_d16ddd87056243ab97dc9555bf5307e0 = L.marker(
                [-13.7667988, 40.2955663],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_567e037ff6c245fc983f483a3c000335 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_d16ddd87056243ab97dc9555bf5307e0.setIcon(custom_icon_567e037ff6c245fc983f483a3c000335);
        
    
            var marker_64282f1603734cd58d87b46e23860af0 = L.marker(
                [-25.4961645, 32.6523462],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_b48d8f2fe8cb48ffaf5af3a62697456c = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_64282f1603734cd58d87b46e23860af0.setIcon(custom_icon_b48d8f2fe8cb48ffaf5af3a62697456c);
        
    
            var marker_a0db37ad3b4f4675bd99574d35c11136 = L.marker(
                [-15.6305199, 37.6833949],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_695379645397462caed408cb1736de16 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_a0db37ad3b4f4675bd99574d35c11136.setIcon(custom_icon_695379645397462caed408cb1736de16);
        
    
            var marker_b1c57582e7154f22b4c71a78c6c0273a = L.marker(
                [-16.4253275, 39.2198785],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_63524ff6b0124c33b8c869a482ff8883 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_b1c57582e7154f22b4c71a78c6c0273a.setIcon(custom_icon_63524ff6b0124c33b8c869a482ff8883);
        
    
            var marker_bafbc54a8a824420a22329a9f7465400 = L.marker(
                [-12.480003, 36.0606587],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_03a1f27e6c7641f682785b050ffdb788 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_bafbc54a8a824420a22329a9f7465400.setIcon(custom_icon_03a1f27e6c7641f682785b050ffdb788);
        
    
            var marker_dbe395c5fe814cf6b85a130c6bfe7c61 = L.marker(
                [-14.6586838, 38.8878036],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_313ecef247494d33a53f620a115231fd = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_dbe395c5fe814cf6b85a130c6bfe7c61.setIcon(custom_icon_313ecef247494d33a53f620a115231fd);
        
    
            var marker_236f34933ce34055948294f203be2903 = L.marker(
                [-16.6445655, 36.3213276],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_6382b106ceba4bc9a382ce64fc9fb31c = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_236f34933ce34055948294f203be2903.setIcon(custom_icon_6382b106ceba4bc9a382ce64fc9fb31c);
        
    
            var marker_b23292db13114814ba7825fadf290f39 = L.marker(
                [-25.9622867, 32.4589721],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_56fb01c535d348af9cea8cad31f8a3bc = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_b23292db13114814ba7825fadf290f39.setIcon(custom_icon_56fb01c535d348af9cea8cad31f8a3bc);
        
    
            var marker_b03fda696f3a4d049d222277db911a33 = L.marker(
                [-25.0293886, 32.64966],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_005caa9d2eb24f4dae26d1839599f1f3 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_b03fda696f3a4d049d222277db911a33.setIcon(custom_icon_005caa9d2eb24f4dae26d1839599f1f3);
        
    
            var marker_0547f9a8649c41378d2af3a3ce62973f = L.marker(
                [-12.5668289, 36.5375689],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_4c604497acc3415d9369005837491778 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_0547f9a8649c41378d2af3a3ce62973f.setIcon(custom_icon_4c604497acc3415d9369005837491778);
        
    
            var marker_bb4ad403ad6c4f9fb85d6ed3aaa24243 = L.marker(
                [-15.7002595, 32.5477547],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_be90c7e3da844482b15b84627b22612d = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_bb4ad403ad6c4f9fb85d6ed3aaa24243.setIcon(custom_icon_be90c7e3da844482b15b84627b22612d);
        
    
            var marker_58c4d1813e1f4f6087fef4dc776e1676 = L.marker(
                [-13.3965439, 37.7378641],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_fb565a24a348462685cd0b9f1f0b3c8a = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_58c4d1813e1f4f6087fef4dc776e1676.setIcon(custom_icon_fb565a24a348462685cd0b9f1f0b3c8a);
        
    
            var marker_7f1fddcf35244815955538003d8bcfdc = L.marker(
                [-25.4087698, 32.8078446],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_7e706049d94f47238c22c55b496a1f2f = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_7f1fddcf35244815955538003d8bcfdc.setIcon(custom_icon_7e706049d94f47238c22c55b496a1f2f);
        
    
            var marker_74821c48a1aa41f8a51f43fef2256caf = L.marker(
                [-14.3514002, 40.4418475],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_19873b10b4d146b2849dfded7a9dd39b = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_74821c48a1aa41f8a51f43fef2256caf.setIcon(custom_icon_19873b10b4d146b2849dfded7a9dd39b);
        
    
            var marker_87ca6858300c456fb46a096272ed5bfe = L.marker(
                [-25.8857352, 32.5119594],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_1938a99588274fd589cd2ce52c44bd3f = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_87ca6858300c456fb46a096272ed5bfe.setIcon(custom_icon_1938a99588274fd589cd2ce52c44bd3f);
        
    
            var marker_bf1d62cd78df4e7a9bf14bbb235a6604 = L.marker(
                [-13.0053993, 35.5508217],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_cca81bb490e74a808a958537f7632f8a = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_bf1d62cd78df4e7a9bf14bbb235a6604.setIcon(custom_icon_cca81bb490e74a808a958537f7632f8a);
        
    
            var marker_9f88fd985caa4b6ca5934d17872580fa = L.marker(
                [-26.1941354, 32.2173911],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_8f144990da78433ba83a3e857a5f12c4 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_9f88fd985caa4b6ca5934d17872580fa.setIcon(custom_icon_8f144990da78433ba83a3e857a5f12c4);
        
    
            var marker_53e16ff54bcb4a6a9d0b7521c3b78dd6 = L.marker(
                [-17.2443345, 37.2003204],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_cd2dc1765c9742238bf4d1d60fe0eb6a = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_53e16ff54bcb4a6a9d0b7521c3b78dd6.setIcon(custom_icon_cd2dc1765c9742238bf4d1d60fe0eb6a);
        
    
            var marker_48989e9a503646e68b0615a56490a50e = L.marker(
                [-16.48014, 39.7173865],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_031a634defcb465c9ab03adde5fe4597 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_48989e9a503646e68b0615a56490a50e.setIcon(custom_icon_031a634defcb465c9ab03adde5fe4597);
        
    
            var marker_0a1f5d1676dc4d1c9388862b38caa459 = L.marker(
                [-14.9824562, 38.0712911],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_59b19d8a39eb4699b4b3126dfb2c0a0d = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_0a1f5d1676dc4d1c9388862b38caa459.setIcon(custom_icon_59b19d8a39eb4699b4b3126dfb2c0a0d);
        
    
            var marker_6607b2ed31df4caf8852ccf45f6b5587 = L.marker(
                [-13.7671059, 40.295914],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_2a948d5efd9c4f628e15a91d435c5cba = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_6607b2ed31df4caf8852ccf45f6b5587.setIcon(custom_icon_2a948d5efd9c4f628e15a91d435c5cba);
        
    
            var marker_f82bbf94597d4703947e168094199906 = L.marker(
                [-14.5775496, 39.5757668],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_76841c3cbe8740169fb4ad1699a78243 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_f82bbf94597d4703947e168094199906.setIcon(custom_icon_76841c3cbe8740169fb4ad1699a78243);
        
    
            var marker_1501c180b4d64a699ca2ec4956763310 = L.marker(
                [-14.7189233, 40.3344073],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_4209993061364b1495ce1cf4a9e0d80d = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_1501c180b4d64a699ca2ec4956763310.setIcon(custom_icon_4209993061364b1495ce1cf4a9e0d80d);
        
    
            var marker_8dc50a727b854e6ebb4ec0080e236463 = L.marker(
                [-12.7406319, 37.7211995],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_bf618085c69043c8be21325e74f71d61 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_8dc50a727b854e6ebb4ec0080e236463.setIcon(custom_icon_bf618085c69043c8be21325e74f71d61);
        
    
            var marker_d9e1690f0c7b4d8ab95512a7c774a26f = L.marker(
                [-15.8352474, 38.9724837],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_0bdc7438745b4a2cbdabe7a9a36f3da7 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_d9e1690f0c7b4d8ab95512a7c774a26f.setIcon(custom_icon_0bdc7438745b4a2cbdabe7a9a36f3da7);
        
    
            var marker_8849320e843d495ba660b136e2e174b6 = L.marker(
                [-15.0034694, 38.5104526],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_302ca9cff2b74272922feb92e16c8597 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_8849320e843d495ba660b136e2e174b6.setIcon(custom_icon_302ca9cff2b74272922feb92e16c8597);
        
    
            var marker_6386812d6eb3401bb6637a15aad4d5dd = L.marker(
                [-15.2541724, 39.2484225],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ee210074a0324597b54251b37e6841c4 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_6386812d6eb3401bb6637a15aad4d5dd.setIcon(custom_icon_ee210074a0324597b54251b37e6841c4);
        
    
            var marker_67bb74e0f4a04998b0aabafce85eedcb = L.marker(
                [-16.4779511, 39.7151028],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_1ccd0e6178fb44c1bb27518fdc756e66 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_67bb74e0f4a04998b0aabafce85eedcb.setIcon(custom_icon_1ccd0e6178fb44c1bb27518fdc756e66);
        
    
            var marker_d17f8951cdf04f2f894911ff4ad69a4a = L.marker(
                [-16.5638037, 39.0775725],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_df495dcb1e4e472fa65bd4898d92f4ff = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_d17f8951cdf04f2f894911ff4ad69a4a.setIcon(custom_icon_df495dcb1e4e472fa65bd4898d92f4ff);
        
    
            var marker_bfb6966517e64f95a836eb6ff59e084c = L.marker(
                [-14.8697478, 37.4996409],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_328fe986f918485eafe1feed09b969ab = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_bfb6966517e64f95a836eb6ff59e084c.setIcon(custom_icon_328fe986f918485eafe1feed09b969ab);
        
    
            var marker_8ecca09fad12486894e462105625289a = L.marker(
                [-15.9647551, 39.5116306],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_5711f5f8606145b09d1713614988e7ef = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_8ecca09fad12486894e462105625289a.setIcon(custom_icon_5711f5f8606145b09d1713614988e7ef);
        
    
            var marker_0aeb41a3ed754b8eb552581e10f392da = L.marker(
                [-16.0592879, 39.7273963],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_e885c1db0b6f43059b8105df5423d2a2 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_0aeb41a3ed754b8eb552581e10f392da.setIcon(custom_icon_e885c1db0b6f43059b8105df5423d2a2);
        
    
            var marker_3e9dfb185f074e2da514fdd57d715276 = L.marker(
                [-14.0637895, 39.4515897],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_99d4bce721414e1f979601013bc36c90 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_3e9dfb185f074e2da514fdd57d715276.setIcon(custom_icon_99d4bce721414e1f979601013bc36c90);
        
    
            var marker_b9b88333bca04b04aca3520c0af997c6 = L.marker(
                [-14.9268121, 38.6633304],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_852d3663fdae4824b0155d21cba3e87f = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_b9b88333bca04b04aca3520c0af997c6.setIcon(custom_icon_852d3663fdae4824b0155d21cba3e87f);
        
    
            var marker_23e829ebd6c249d0a452729782d1f78e = L.marker(
                [-15.5685939, 40.4087611],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_02fec705c0084422921c732d19d49438 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_23e829ebd6c249d0a452729782d1f78e.setIcon(custom_icon_02fec705c0084422921c732d19d49438);
        
    
            var marker_98e51358a911499686e484346c178f34 = L.marker(
                [-14.9238751, 39.9946303],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_5e9bc21fe60146abaa3b1de9bea1fb49 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_98e51358a911499686e484346c178f34.setIcon(custom_icon_5e9bc21fe60146abaa3b1de9bea1fb49);
        
    
            var marker_29a0bdf774634137bbf80342ec3d41f7 = L.marker(
                [-15.7087624, 39.3378501],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_d36c8cfbc46e4dd0b10be0cc58dd27ff = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_29a0bdf774634137bbf80342ec3d41f7.setIcon(custom_icon_d36c8cfbc46e4dd0b10be0cc58dd27ff);
        
    
            var marker_715f4dbe3e3f477cbe4cc4d13131d4a4 = L.marker(
                [-15.9010538, 39.8644138],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_e7114812bd58466ba46a7e225e517562 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_715f4dbe3e3f477cbe4cc4d13131d4a4.setIcon(custom_icon_e7114812bd58466ba46a7e225e517562);
        
    
            var marker_fb848b354cca43ee8665cbea7d0359b9 = L.marker(
                [-15.274339, 39.0412484],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_9284bc0f3066471c893c8482c8ef9d4d = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_fb848b354cca43ee8665cbea7d0359b9.setIcon(custom_icon_9284bc0f3066471c893c8482c8ef9d4d);
        
    
            var marker_ab3fc84269b64cd0b3e9318d1b2021a8 = L.marker(
                [-14.3514106, 40.4418455],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_2c29621fe7f349a3abb5c5aae7d95905 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_ab3fc84269b64cd0b3e9318d1b2021a8.setIcon(custom_icon_2c29621fe7f349a3abb5c5aae7d95905);
        
    
            var marker_53cbf96213124935a8e7eaefc323b7ef = L.marker(
                [-14.9372771, 37.1766443],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_aaed7f885a184107986741fe22c9303a = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_53cbf96213124935a8e7eaefc323b7ef.setIcon(custom_icon_aaed7f885a184107986741fe22c9303a);
        
    
            var marker_7ac88f9508f149e0b84b4e92da4c533b = L.marker(
                [-14.8165669, 38.965944],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_60e99fef64974216be8199bf713aa380 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_7ac88f9508f149e0b84b4e92da4c533b.setIcon(custom_icon_60e99fef64974216be8199bf713aa380);
        
    
            var marker_bff8ea17558e4637a58d697f1be4646b = L.marker(
                [-14.4216951, 39.9247527],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_f2debdb5b1144a2d9bb7871dd3eb656d = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_bff8ea17558e4637a58d697f1be4646b.setIcon(custom_icon_f2debdb5b1144a2d9bb7871dd3eb656d);
        
    
            var marker_00575cadd9c04ebca616d1399050f173 = L.marker(
                [-14.7753884, 40.7296446],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_94652ebde4ba4dc1a4c1e281fc5e4ab1 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_00575cadd9c04ebca616d1399050f173.setIcon(custom_icon_94652ebde4ba4dc1a4c1e281fc5e4ab1);
        
    
            var marker_1256dae616024bd78246d671fb5f7b38 = L.marker(
                [-15.0082143, 39.6811608],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_e4bcc56c4f674a5fbf1a1954e6e5bbdb = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_1256dae616024bd78246d671fb5f7b38.setIcon(custom_icon_e4bcc56c4f674a5fbf1a1954e6e5bbdb);
        
    
            var marker_6326e6cce6b24dde8d674915390641ad = L.marker(
                [-14.3693372, 39.923076],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_98cd9f4ef158440fb80434bb904b52ed = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_6326e6cce6b24dde8d674915390641ad.setIcon(custom_icon_98cd9f4ef158440fb80434bb904b52ed);
        
    
            var marker_8e324ca2f6234872806492b0b9984fe5 = L.marker(
                [-14.5512962, 40.6219313],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_b7220906a47f451f9b2e5348c2003fa2 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_8e324ca2f6234872806492b0b9984fe5.setIcon(custom_icon_b7220906a47f451f9b2e5348c2003fa2);
        
    
            var marker_0a4cd2431995468cafd7435cd1c96446 = L.marker(
                [-15.4578652, 38.6767103],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_440cb5dabcfc495ca9b3d00df314a463 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_0a4cd2431995468cafd7435cd1c96446.setIcon(custom_icon_440cb5dabcfc495ca9b3d00df314a463);
        
    
            var marker_028504db769641859a79dcb75cd123dd = L.marker(
                [-14.6611147, 40.6801244],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_4578b8cce7a346a89ebe1c0ad54a7d37 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_028504db769641859a79dcb75cd123dd.setIcon(custom_icon_4578b8cce7a346a89ebe1c0ad54a7d37);
        
    
            var marker_5f3c9520cf6a4641bef2aae7bf42185f = L.marker(
                [-15.8827077, 39.0720059],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_4d5bd6f9e65945268625dd42a68a1bc3 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_5f3c9520cf6a4641bef2aae7bf42185f.setIcon(custom_icon_4d5bd6f9e65945268625dd42a68a1bc3);
        
    
            var marker_1be1539f11fe48828dd74a978b15e055 = L.marker(
                [-14.4772624, 38.9157243],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_b07cf3695bd448a7bc013b191d41018b = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_1be1539f11fe48828dd74a978b15e055.setIcon(custom_icon_b07cf3695bd448a7bc013b191d41018b);
        
    
            var marker_e06cc3a967554b42a38b0db14190560d = L.marker(
                [-14.2251655, 38.3219403],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ce5dd38588d147258f0161445a647ab5 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_e06cc3a967554b42a38b0db14190560d.setIcon(custom_icon_ce5dd38588d147258f0161445a647ab5);
        
    
            var marker_a7f9bfca00ae44f6be38885b13fd1d43 = L.marker(
                [-24.4911803, 32.0877606],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_39bd4e86a3b742888c5a95e1dbb50b77 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_a7f9bfca00ae44f6be38885b13fd1d43.setIcon(custom_icon_39bd4e86a3b742888c5a95e1dbb50b77);
        
    
            var marker_830783bb946845e9bf8f56328f85721d = L.marker(
                [-16.3657571, 39.7500349],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_66a88d522a084ccd9eb6112e3c3f33a5 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_830783bb946845e9bf8f56328f85721d.setIcon(custom_icon_66a88d522a084ccd9eb6112e3c3f33a5);
        
    
            var marker_c0aa39ef6b5440f8b3b8baa759ca4d38 = L.marker(
                [-14.3174998, 35.8588976],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_dbcd877288704bc5bb57bd465d8a541a = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_c0aa39ef6b5440f8b3b8baa759ca4d38.setIcon(custom_icon_dbcd877288704bc5bb57bd465d8a541a);
        
    
            var marker_f8e3ef09a0a94244a927162a63cfd90c = L.marker(
                [-13.9286224, 40.5962124],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ffd6886a1d9c494ebd2bca7ec3779c65 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_f8e3ef09a0a94244a927162a63cfd90c.setIcon(custom_icon_ffd6886a1d9c494ebd2bca7ec3779c65);
        
    
            var marker_f2e210f191794430b287009584cd7245 = L.marker(
                [-26.1589788, 32.346331],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a53c6b8ea98b49a7b539ad00c8590ab2 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_f2e210f191794430b287009584cd7245.setIcon(custom_icon_a53c6b8ea98b49a7b539ad00c8590ab2);
        
    
            var marker_9f7344cb28f14316b0ca46c9e22d490b = L.marker(
                [-13.023861, 34.9548335],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_6b4ffbca85d6483885f64a4928ad427d = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_9f7344cb28f14316b0ca46c9e22d490b.setIcon(custom_icon_6b4ffbca85d6483885f64a4928ad427d);
        
    
            var marker_d5f32697d2054cbcb0f31d9a0947eb95 = L.marker(
                [-16.1467148, 38.3724987],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_8fe49343aa6f44d3aad05126cab47587 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_d5f32697d2054cbcb0f31d9a0947eb95.setIcon(custom_icon_8fe49343aa6f44d3aad05126cab47587);
        
    
            var marker_4b92af45e260419b8b57c4e2351b48a8 = L.marker(
                [-14.2119049, 40.7085468],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_952a50aeddec4b98ba479e38fa0bd0bd = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_4b92af45e260419b8b57c4e2351b48a8.setIcon(custom_icon_952a50aeddec4b98ba479e38fa0bd0bd);
        
    
            var marker_69b2ffe5a4ab442e9f2a5b1e03eb4b9e = L.marker(
                [-14.1723103, 38.7401989],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_4fad3aa93fcb42b0919fbc8d12758f46 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_69b2ffe5a4ab442e9f2a5b1e03eb4b9e.setIcon(custom_icon_4fad3aa93fcb42b0919fbc8d12758f46);
        
    
            var marker_289c9e944bc744b186c76edcbf7f4e29 = L.marker(
                [-17.4822352, 37.1996645],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_302e3446181142d79c4b4813148a9010 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_289c9e944bc744b186c76edcbf7f4e29.setIcon(custom_icon_302e3446181142d79c4b4813148a9010);
        
    
            var marker_e14710d1b20e41f4b6c72185a59d6c14 = L.marker(
                [-14.9968881, 38.9519942],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_d305d4e97d37422ea827363c1ee4fa08 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_e14710d1b20e41f4b6c72185a59d6c14.setIcon(custom_icon_d305d4e97d37422ea827363c1ee4fa08);
        
    
            var marker_63b05308435a430fac64e2222b7ca976 = L.marker(
                [-20.1497002, 34.1497002],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_45c6db3eade5429d8c78dcf752a48b30 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_63b05308435a430fac64e2222b7ca976.setIcon(custom_icon_45c6db3eade5429d8c78dcf752a48b30);
        
    
            var marker_cb8d5e70981843e5974ab689a79dcd86 = L.marker(
                [-14.0249168, 35.365866],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_09d210286a1e402ea4b4fa76d644fb80 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_cb8d5e70981843e5974ab689a79dcd86.setIcon(custom_icon_09d210286a1e402ea4b4fa76d644fb80);
        
    
            var marker_16780b33d72048eb93ca95e2a8f813e6 = L.marker(
                [-26.342666, 32.675035],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_37daa302928049bca9bfe59c6ef7a0a6 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_16780b33d72048eb93ca95e2a8f813e6.setIcon(custom_icon_37daa302928049bca9bfe59c6ef7a0a6);
        
    
            var marker_631547655cf748809fc42c9d2d7edb5a = L.marker(
                [-15.3298079, 39.1518188],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_6ae6f754ee224b3db549427df18812a1 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_631547655cf748809fc42c9d2d7edb5a.setIcon(custom_icon_6ae6f754ee224b3db549427df18812a1);
        
    
            var marker_dd3ac1be77cb4a49b39f6882a449d60f = L.marker(
                [-14.5988968, 38.7951715],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_2edfffca1def4a838763d0e58f2039c5 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_dd3ac1be77cb4a49b39f6882a449d60f.setIcon(custom_icon_2edfffca1def4a838763d0e58f2039c5);
        
    
            var marker_8db2018f31ca4c8b82419af44e19fcea = L.marker(
                [-14.520968, 38.895818],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_5f83af37dbfa47b38054e74bdf5b3f2f = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_8db2018f31ca4c8b82419af44e19fcea.setIcon(custom_icon_5f83af37dbfa47b38054e74bdf5b3f2f);
        
    
            var marker_2ec1188f4f334193beeaf09947b8c4ab = L.marker(
                [-15.1735628, 39.4629349],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_5e216e0c6d22498db388f358f8a9b79a = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_2ec1188f4f334193beeaf09947b8c4ab.setIcon(custom_icon_5e216e0c6d22498db388f358f8a9b79a);
        
    
            var marker_b91afff84b844434abaea7e7f91ebf9d = L.marker(
                [-14.9751666, 38.8150299],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_da98a4447f134ba1a5543b10b24054bf = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_b91afff84b844434abaea7e7f91ebf9d.setIcon(custom_icon_da98a4447f134ba1a5543b10b24054bf);
        
    
            var marker_29638b96167f4d08b46d1995c6a120bf = L.marker(
                [-14.7947246, 38.370333],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_077fc309732349f795e391333c5d62fc = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_29638b96167f4d08b46d1995c6a120bf.setIcon(custom_icon_077fc309732349f795e391333c5d62fc);
        
    
            var marker_bece65ca308348999090146c013058a6 = L.marker(
                [-14.019413, 40.3452703],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_c211880e38a94c14bbd13147242269ff = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_bece65ca308348999090146c013058a6.setIcon(custom_icon_c211880e38a94c14bbd13147242269ff);
        
    
            var marker_1a8b0bc4f7354c5f9bef6a43beb1a074 = L.marker(
                [-16.3442248, 39.9200799],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_5fce8813c9504c25b8d20ca177677513 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_1a8b0bc4f7354c5f9bef6a43beb1a074.setIcon(custom_icon_5fce8813c9504c25b8d20ca177677513);
        
    
            var marker_0fe957023bc740b0bdaf3d36ce13ddaf = L.marker(
                [-14.3369017, 39.9055128],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_5f6bc35d6ffc4b96b3622bae9b488e8e = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_0fe957023bc740b0bdaf3d36ce13ddaf.setIcon(custom_icon_5f6bc35d6ffc4b96b3622bae9b488e8e);
        
    
            var marker_2e7a235dbdb8480389b397de81d95447 = L.marker(
                [-15.2037448, 39.3879564],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a6f0c9fe5c1d4c3998e5dd44217d84aa = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_2e7a235dbdb8480389b397de81d95447.setIcon(custom_icon_a6f0c9fe5c1d4c3998e5dd44217d84aa);
        
    
            var marker_029933297f90494c8cf6e1af02e6e8d6 = L.marker(
                [-15.9951704, 39.7374281],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_60652bf4cd5745ef89c65859b4096589 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_029933297f90494c8cf6e1af02e6e8d6.setIcon(custom_icon_60652bf4cd5745ef89c65859b4096589);
        
    
            var marker_6fc164336c7a499d8b959c90257e7592 = L.marker(
                [-15.2284471, 39.1180229],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_f19d3fd43ffa4667b0720316a98c0b52 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_6fc164336c7a499d8b959c90257e7592.setIcon(custom_icon_f19d3fd43ffa4667b0720316a98c0b52);
        
    
            var marker_8fd9fd67f5e04faf8ca866b36101c586 = L.marker(
                [-16.4136553, 39.427926],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a504edff637a4947b9cd5807c584e3bf = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_8fd9fd67f5e04faf8ca866b36101c586.setIcon(custom_icon_a504edff637a4947b9cd5807c584e3bf);
        
    
            var marker_364b6fe9ace94b258a39c2832ee09a26 = L.marker(
                [-15.2304767, 38.9742532],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_e4b74e571c4243359493a956d2ac4d89 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_364b6fe9ace94b258a39c2832ee09a26.setIcon(custom_icon_e4b74e571c4243359493a956d2ac4d89);
        
    
            var marker_a393feb5e4df481c8f5c4d6fdfa40035 = L.marker(
                [-15.5864231, 38.574653],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_2c90187fa7ee4943ad84f45fa83eefeb = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_a393feb5e4df481c8f5c4d6fdfa40035.setIcon(custom_icon_2c90187fa7ee4943ad84f45fa83eefeb);
        
    
            var marker_2da36dc77abf4ac68e943a982c55b141 = L.marker(
                [-15.3370016, 39.3396056],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_29098f5bc23b41eb826fb1d810217f13 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_2da36dc77abf4ac68e943a982c55b141.setIcon(custom_icon_29098f5bc23b41eb826fb1d810217f13);
        
    
            var marker_05765ebb7e9b4bb3be6ab9469aadde9f = L.marker(
                [-15.8704186, 39.7426584],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_47d24f0a4c95461c8b6f6c0f62b7e34b = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_05765ebb7e9b4bb3be6ab9469aadde9f.setIcon(custom_icon_47d24f0a4c95461c8b6f6c0f62b7e34b);
        
    
            var marker_9850ac42ac2f4a888e11687da20a658f = L.marker(
                [-24.7995012, 32.8592384],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a946c76ba0c249c0b9e76e05916c8e5f = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_9850ac42ac2f4a888e11687da20a658f.setIcon(custom_icon_a946c76ba0c249c0b9e76e05916c8e5f);
        
    
            var marker_5bb7d50775924ceca6181f514ac46138 = L.marker(
                [-16.968006, 36.1180791],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_4cd7061f41804cea9107510ba0627d89 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_5bb7d50775924ceca6181f514ac46138.setIcon(custom_icon_4cd7061f41804cea9107510ba0627d89);
        
    
            var marker_d814a8f0220a49dd945dbc82b9c18f2f = L.marker(
                [-13.4261157, 36.1987549],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_c310150a7da84c559c159e6f800650d5 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_d814a8f0220a49dd945dbc82b9c18f2f.setIcon(custom_icon_c310150a7da84c559c159e6f800650d5);
        
    
            var marker_fda3d9856f77414d9db8ed83835eb2df = L.marker(
                [-14.6414088, 39.1051295],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_584987a875944a2f8ffdc2ae8ac2d57c = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_fda3d9856f77414d9db8ed83835eb2df.setIcon(custom_icon_584987a875944a2f8ffdc2ae8ac2d57c);
        
    
            var marker_f46f51a1db674520b19553842262bf99 = L.marker(
                [-18.611128, 36.4315706],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_10b34f8d427c43739d6eb58ee054a18a = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_f46f51a1db674520b19553842262bf99.setIcon(custom_icon_10b34f8d427c43739d6eb58ee054a18a);
        
    
            var marker_02df9bf5f2744dd99bf546eeca402ae5 = L.marker(
                [-13.473642, 36.3038599],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_26e6ac6d597d4862adb627f254f86c79 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_02df9bf5f2744dd99bf546eeca402ae5.setIcon(custom_icon_26e6ac6d597d4862adb627f254f86c79);
        
    
            var marker_0188fdb2d9b940f884f16c2c245014ac = L.marker(
                [-25.456927, 32.7756929],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_4af560ae308346aa8355f3e8083e046e = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_0188fdb2d9b940f884f16c2c245014ac.setIcon(custom_icon_4af560ae308346aa8355f3e8083e046e);
        
    
            var marker_36e762e9d9b145c2bdd7510a5cf108e1 = L.marker(
                [-19.2422349, 34.4728372],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_f1ff1256f6334cc49ba8d4cfb6ca1d0c = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_36e762e9d9b145c2bdd7510a5cf108e1.setIcon(custom_icon_f1ff1256f6334cc49ba8d4cfb6ca1d0c);
        
    
            var marker_4d50135330d648e2a0d62fba7d095e31 = L.marker(
                [-18.5293369, 35.2220306],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ab89f8dad1dd43bc85365e5a52871797 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_4d50135330d648e2a0d62fba7d095e31.setIcon(custom_icon_ab89f8dad1dd43bc85365e5a52871797);
        
    
            var marker_0fe3f0e1c0e8452f8ce6efbf1a3ca1dc = L.marker(
                [-19.6506004, 34.7658005],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_65bc96bc35f94338b9f487dda5b3d584 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_0fe3f0e1c0e8452f8ce6efbf1a3ca1dc.setIcon(custom_icon_65bc96bc35f94338b9f487dda5b3d584);
        
    
            var marker_d3eff4ac5c534617ac1ca2217c3e5120 = L.marker(
                [-17.8502998, 35.3986015],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_33799ba8455c42da8a37bc9b59c27abe = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_d3eff4ac5c534617ac1ca2217c3e5120.setIcon(custom_icon_33799ba8455c42da8a37bc9b59c27abe);
        
    
            var marker_9dda71431ad64bb79eddab0e496ade64 = L.marker(
                [-17.7828007, 35.2468987],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_f97da86e57b04940bae599c2fb849aef = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_9dda71431ad64bb79eddab0e496ade64.setIcon(custom_icon_f97da86e57b04940bae599c2fb849aef);
        
    
            var marker_fb23603f88e24bb689ecdc3a4532f566 = L.marker(
                [-20.3270623, 33.8856862],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_3b95b633b52848f9a6476f78963a4dc0 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_fb23603f88e24bb689ecdc3a4532f566.setIcon(custom_icon_3b95b633b52848f9a6476f78963a4dc0);
        
    
            var marker_f98b85afb6be4bfb950c3c01f1957ce0 = L.marker(
                [-19.950304, 34.0630727],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_361e4a6de98a424e9d07a32facfc0306 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_f98b85afb6be4bfb950c3c01f1957ce0.setIcon(custom_icon_361e4a6de98a424e9d07a32facfc0306);
        
    
            var marker_cb9748c75aba448e87e26f024c28d2f4 = L.marker(
                [-18.2238998, 36.0792007],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_b4cab3ffceb34997a1451765c6ed12d4 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_cb9748c75aba448e87e26f024c28d2f4.setIcon(custom_icon_b4cab3ffceb34997a1451765c6ed12d4);
        
    
            var marker_18b8eb6e025d440e8f0dced41a02e97a = L.marker(
                [-19.360051, 34.3564648],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_cd145fb62ac54912818de9270696ebd4 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_18b8eb6e025d440e8f0dced41a02e97a.setIcon(custom_icon_cd145fb62ac54912818de9270696ebd4);
        
    
            var marker_9ce9826836354fc2adc42a3718a5b83f = L.marker(
                [-15.5612044, 37.5904738],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a7255bf752fa4d17a5f54a14dbb61322 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_9ce9826836354fc2adc42a3718a5b83f.setIcon(custom_icon_a7255bf752fa4d17a5f54a14dbb61322);
        
    
            var marker_e8b7220f570c43d8afa0922e9996d316 = L.marker(
                [-18.5474243, 34.1767267],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_e8b4c4d5080446b48a3c2d2aaeec7af4 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_e8b7220f570c43d8afa0922e9996d316.setIcon(custom_icon_e8b4c4d5080446b48a3c2d2aaeec7af4);
        
    
            var marker_9f760540c926464ba617f11287b9bbf9 = L.marker(
                [-19.8847109, 34.5843972],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_0a52c3da91c848e2a4c9c4c3b195a117 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_9f760540c926464ba617f11287b9bbf9.setIcon(custom_icon_0a52c3da91c848e2a4c9c4c3b195a117);
        
    
            var marker_8e4b179dc3dd48978f8bddb194bf5702 = L.marker(
                [-17.8668995, 35.3116989],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_d911b727460f4c8792355a84ddb47e5a = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_8e4b179dc3dd48978f8bddb194bf5702.setIcon(custom_icon_d911b727460f4c8792355a84ddb47e5a);
        
    
            var marker_9fb314f91e66468dbdadaaf58247ed1b = L.marker(
                [-17.8586578, 34.4843826],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_c2d0c8b14b7b4834829eddb62c799403 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_9fb314f91e66468dbdadaaf58247ed1b.setIcon(custom_icon_c2d0c8b14b7b4834829eddb62c799403);
        
    
            var marker_2dfef311346944e99a9a40e5670126b6 = L.marker(
                [-17.6844006, 35.0388985],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_cbbe7b89c6f2413a8b43cda8428e0753 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_2dfef311346944e99a9a40e5670126b6.setIcon(custom_icon_cbbe7b89c6f2413a8b43cda8428e0753);
        
    
            var marker_43e3a2e1781843939486a0c2efe8150b = L.marker(
                [-22.489034, 32.8794633],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_7f1299ff7b7e4c28874eda8a5d0c62eb = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_43e3a2e1781843939486a0c2efe8150b.setIcon(custom_icon_7f1299ff7b7e4c28874eda8a5d0c62eb);
        
    
            var marker_f17b9fdb7d994a9ab8ee82cec2ef185c = L.marker(
                [-21.9924054, 32.9133645],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_1fe270d12c604335937623ac05c285d7 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_f17b9fdb7d994a9ab8ee82cec2ef185c.setIcon(custom_icon_1fe270d12c604335937623ac05c285d7);
        
    
            var marker_629e2db9a7bb4eca82f7547fab0a4fd7 = L.marker(
                [-20.218741, 33.5461655],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ad0531855ebc43b7990186b019a0f077 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_629e2db9a7bb4eca82f7547fab0a4fd7.setIcon(custom_icon_ad0531855ebc43b7990186b019a0f077);
        
    
            var marker_c1c9115882424442b47ed451f77d3fc3 = L.marker(
                [-22.4950375, 32.1821633],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_5b7d6b850e854081a0eb977e739b8669 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_c1c9115882424442b47ed451f77d3fc3.setIcon(custom_icon_5b7d6b850e854081a0eb977e739b8669);
        
    
            var marker_594478fc0e624fc2810a5e037c113ba0 = L.marker(
                [-22.658585, 32.0333481],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_b6102a2694214c589c4dbab7ac7a439c = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_594478fc0e624fc2810a5e037c113ba0.setIcon(custom_icon_b6102a2694214c589c4dbab7ac7a439c);
        
    
            var marker_25bd44a3b07f4851937fbf96921a96a8 = L.marker(
                [-21.7093112, 32.5056649],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_679844fc7f9f4a089975ca717a7c200e = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_25bd44a3b07f4851937fbf96921a96a8.setIcon(custom_icon_679844fc7f9f4a089975ca717a7c200e);
        
    
            var marker_f2285c1fdbf74e43900e295e2da283c3 = L.marker(
                [-17.9602587, 35.7379037],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_8153bf94f57d419dbe122ac507da583b = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_f2285c1fdbf74e43900e295e2da283c3.setIcon(custom_icon_8153bf94f57d419dbe122ac507da583b);
        
    
            var marker_28ddbd617cd641f6aee97cd661ad24e0 = L.marker(
                [-20.2351055, 33.4592629],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_7e3709f5a84c4a4a9a74bc11f2a89d27 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_28ddbd617cd641f6aee97cd661ad24e0.setIcon(custom_icon_7e3709f5a84c4a4a9a74bc11f2a89d27);
        
    
            var marker_915e5db61a634038af04bfce20928c85 = L.marker(
                [-13.1918542, 35.3148343],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_68543af1113544dea964eb0622e1e3cc = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_915e5db61a634038af04bfce20928c85.setIcon(custom_icon_68543af1113544dea964eb0622e1e3cc);
        
    
            var marker_2f7f92e0de9043fab04c8e49fa69dd45 = L.marker(
                [-25.6450688, 32.4974392],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_b031e0e07ba74e8a933fd01d19adcb48 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_2f7f92e0de9043fab04c8e49fa69dd45.setIcon(custom_icon_b031e0e07ba74e8a933fd01d19adcb48);
        
    
            var marker_31ecf2c71cd049b2812ed92004d26a3f = L.marker(
                [-14.8034884, 40.2273634],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_aee4329d874b4d999841bfe2964cc04d = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_31ecf2c71cd049b2812ed92004d26a3f.setIcon(custom_icon_aee4329d874b4d999841bfe2964cc04d);
        
    
            var marker_8a8bf2119d104d99bcc55b132a57c8a9 = L.marker(
                [-17.5595145, 36.9376686],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_1c587ec2634c426f84ea33259a270a93 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_8a8bf2119d104d99bcc55b132a57c8a9.setIcon(custom_icon_1c587ec2634c426f84ea33259a270a93);
        
    
            var marker_23e0bd76a7b2428b97f7386ad82bede4 = L.marker(
                [-13.7489189, 35.6167799],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_655f301c2e054171a81569dec3e561df = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_23e0bd76a7b2428b97f7386ad82bede4.setIcon(custom_icon_655f301c2e054171a81569dec3e561df);
        
    
            var marker_480083a41fb64a8e8fd34657f4322427 = L.marker(
                [-12.140149, 34.7608904],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_f6a9ea243d424d0cb0271cfae9fc88bb = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_480083a41fb64a8e8fd34657f4322427.setIcon(custom_icon_f6a9ea243d424d0cb0271cfae9fc88bb);
        
    
            var marker_33fd1b80f8ea485b9178007b90caff5c = L.marker(
                [-13.313739, 35.5326196],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_8f3c76b19d1e4fb7a1fad6155e93dd0f = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_33fd1b80f8ea485b9178007b90caff5c.setIcon(custom_icon_8f3c76b19d1e4fb7a1fad6155e93dd0f);
        
    
            var marker_d6826fa5d39545e5994413aba98a885c = L.marker(
                [-17.7023591, 37.0097262],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_f5adf066d973454386901ea61ab796c4 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_d6826fa5d39545e5994413aba98a885c.setIcon(custom_icon_f5adf066d973454386901ea61ab796c4);
        
    
            var marker_c6557131f844480681161941103a6e02 = L.marker(
                [-14.6507938, 35.9375721],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_686bfcd29369478dbd90aff4935dfbdd = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_c6557131f844480681161941103a6e02.setIcon(custom_icon_686bfcd29369478dbd90aff4935dfbdd);
        
    
            var marker_726cd6f27e914c8aa4e63448371f9535 = L.marker(
                [-25.3093395, 32.8330218],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_f8bf7d454c354e5aa8c4f278c470a28e = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_726cd6f27e914c8aa4e63448371f9535.setIcon(custom_icon_f8bf7d454c354e5aa8c4f278c470a28e);
        
    
            var marker_c3a3837f616d4171b62a43eb975efcb4 = L.marker(
                [-14.1332959, 40.1484471],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ed7423e304a04ce9ba4ca45f0ced7510 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_c3a3837f616d4171b62a43eb975efcb4.setIcon(custom_icon_ed7423e304a04ce9ba4ca45f0ced7510);
        
    
            var marker_37db4891bcc2479da6017fc44f78ec66 = L.marker(
                [-16.7625856, 39.2228481],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_c8e4ceb0e0f44dbeb87f1b7760f686ff = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_37db4891bcc2479da6017fc44f78ec66.setIcon(custom_icon_c8e4ceb0e0f44dbeb87f1b7760f686ff);
        
    
            var marker_7a0fade064484ebe84aeb611820be84d = L.marker(
                [-14.4318974, 39.3945751],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_2137a9a58bf440e08aad9a5f7ad5aaf9 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_7a0fade064484ebe84aeb611820be84d.setIcon(custom_icon_2137a9a58bf440e08aad9a5f7ad5aaf9);
        
    
            var marker_a098ae73491d401a8962008ab270d20a = L.marker(
                [-16.0326804, 40.1023994],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_e24b4852932444d6974bd1e0a975d0ee = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_a098ae73491d401a8962008ab270d20a.setIcon(custom_icon_e24b4852932444d6974bd1e0a975d0ee);
        
    
            var marker_9edc104cf6394d4dbceb9dd4359a34bf = L.marker(
                [-14.9047583, 39.3235801],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_842dc44a05bc40059b62ee222b4de87c = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_9edc104cf6394d4dbceb9dd4359a34bf.setIcon(custom_icon_842dc44a05bc40059b62ee222b4de87c);
        
    
            var marker_e559d048778d40da80f5d438f6395fd5 = L.marker(
                [-13.2741252, 35.3641728],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_33438c6f245a4e03870c28c44db883f1 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_e559d048778d40da80f5d438f6395fd5.setIcon(custom_icon_33438c6f245a4e03870c28c44db883f1);
        
    
            var marker_caa0b0409f1f434cb815c5950e497f38 = L.marker(
                [-18.4168534, 35.0167778],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_01cc3514b23342e4ad7b9cc498c61a7a = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_caa0b0409f1f434cb815c5950e497f38.setIcon(custom_icon_01cc3514b23342e4ad7b9cc498c61a7a);
        
    
            var marker_19a15dc435074236a8f9c0fa3c4cd51a = L.marker(
                [-14.8970108, 36.5286981],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_f3a297a6254042a592ff3f32cd1b75be = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_19a15dc435074236a8f9c0fa3c4cd51a.setIcon(custom_icon_f3a297a6254042a592ff3f32cd1b75be);
        
    
            var marker_e26b084f52d64fd197bd08c73b7ed32d = L.marker(
                [-19.8688528, 34.4688642],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_b3698612c20a4ed98d240a286c3f5491 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_e26b084f52d64fd197bd08c73b7ed32d.setIcon(custom_icon_b3698612c20a4ed98d240a286c3f5491);
        
    
            var marker_10c0c0a9f96d49b185a56ba5aae13ffb = L.marker(
                [-20.194886, 33.7038942],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_dba8238bd53642c794238da39baf14dc = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_10c0c0a9f96d49b185a56ba5aae13ffb.setIcon(custom_icon_dba8238bd53642c794238da39baf14dc);
        
    
            var marker_8084d8f680114812ba60d09c186a12cb = L.marker(
                [-20.2897172, 33.6572586],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_65dfc8e99cf54d81aff71f794c5e3ca2 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_8084d8f680114812ba60d09c186a12cb.setIcon(custom_icon_65dfc8e99cf54d81aff71f794c5e3ca2);
        
    
            var marker_68576a3e053c40659a34fcba761aabe0 = L.marker(
                [-18.6931419, 34.072895],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a8a78ffb363b4452b042385dc391c993 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_68576a3e053c40659a34fcba761aabe0.setIcon(custom_icon_a8a78ffb363b4452b042385dc391c993);
        
    
            var marker_6ab90f25ffc141db98f95f1882829d05 = L.marker(
                [-19.6295295, 34.716699],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_27313ca25c274f11a40d5b1820eaa7bf = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_6ab90f25ffc141db98f95f1882829d05.setIcon(custom_icon_27313ca25c274f11a40d5b1820eaa7bf);
        
    
            var marker_af966b2424534a5e98af486503f3d968 = L.marker(
                [-20.025477, 34.7174902],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_5c35f488746b43e3be5d0f073c63344e = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_af966b2424534a5e98af486503f3d968.setIcon(custom_icon_5c35f488746b43e3be5d0f073c63344e);
        
    
            var marker_080585a6002e44ebb509a6887052393e = L.marker(
                [-18.6131037, 34.214051],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_6d776c280b8e49a69d0874207eb2188f = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_080585a6002e44ebb509a6887052393e.setIcon(custom_icon_6d776c280b8e49a69d0874207eb2188f);
        
    
            var marker_ef6745a524da4be3bc4bfa03b2928555 = L.marker(
                [-20.4767315, 33.7014373],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_b864adce487043bf8248afcdb3085144 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_ef6745a524da4be3bc4bfa03b2928555.setIcon(custom_icon_b864adce487043bf8248afcdb3085144);
        
    
            var marker_82af7c1a53a74648bf949b27f9290acd = L.marker(
                [-20.7413045, 34.9263766],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_f91f4f5b93574af3a311fb130962b7fc = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_82af7c1a53a74648bf949b27f9290acd.setIcon(custom_icon_f91f4f5b93574af3a311fb130962b7fc);
        
    
            var marker_b9167b25a7d24519b4a05de9a4d3c299 = L.marker(
                [-16.8902465, 34.6560415],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_6716e2a6f06145b5b46db9c5129e9368 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_b9167b25a7d24519b4a05de9a4d3c299.setIcon(custom_icon_6716e2a6f06145b5b46db9c5129e9368);
        
    
            var marker_7ac1106cfb99416d9131ab6fd640c08d = L.marker(
                [-20.1913668, 33.9075235],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_5f0ef1d328c14aea8a59febed4b01662 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_7ac1106cfb99416d9131ab6fd640c08d.setIcon(custom_icon_5f0ef1d328c14aea8a59febed4b01662);
        
    
            var marker_58a2b5aef2304be6ba16039e437a8d23 = L.marker(
                [-18.8202719, 34.7465044],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_2babcab972844af3b64a6863da443d8b = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_58a2b5aef2304be6ba16039e437a8d23.setIcon(custom_icon_2babcab972844af3b64a6863da443d8b);
        
    
            var marker_54049501061f40e59d1cbf02d7097dab = L.marker(
                [-20.7010335, 34.7932586],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_7244ede49c4a4635a9a15338f0aca8c6 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_54049501061f40e59d1cbf02d7097dab.setIcon(custom_icon_7244ede49c4a4635a9a15338f0aca8c6);
        
    
            var marker_cec8a977d2f443bfabb1fc0b6f9b4db7 = L.marker(
                [-17.9593088, 34.391229],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_17987ff72d364dcdaaa8f0d490659d03 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_cec8a977d2f443bfabb1fc0b6f9b4db7.setIcon(custom_icon_17987ff72d364dcdaaa8f0d490659d03);
        
    
            var marker_904e66d3189d4dc8a519492cb9a0a2e3 = L.marker(
                [-19.9644883, 34.418273],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_b8e50b7548a4484eba6a43559c031fee = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_904e66d3189d4dc8a519492cb9a0a2e3.setIcon(custom_icon_b8e50b7548a4484eba6a43559c031fee);
        
    
            var marker_5a5896a67c754acfab594fe697e9a9c8 = L.marker(
                [-19.5031608, 34.5933449],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_29b95ca970d340c7ba70bc22a504e791 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_5a5896a67c754acfab594fe697e9a9c8.setIcon(custom_icon_29b95ca970d340c7ba70bc22a504e791);
        
    
            var marker_c0987fb69a064c4ea335d092c75016d4 = L.marker(
                [-20.975017, 35.0051156],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_b14fc1b8ca3b42b88ab3491a288a57b5 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_c0987fb69a064c4ea335d092c75016d4.setIcon(custom_icon_b14fc1b8ca3b42b88ab3491a288a57b5);
        
    
            var marker_a38368cb96b942ce8cf565a66d1fed32 = L.marker(
                [-19.2524706, 34.1291698],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_50dea5541e0149a4bebc5e6469bfae82 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_a38368cb96b942ce8cf565a66d1fed32.setIcon(custom_icon_50dea5541e0149a4bebc5e6469bfae82);
        
    
            var marker_c02b59ec692640b199c2e226f35a11f3 = L.marker(
                [-18.5994664, 34.1373096],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ae97b47806e343d48e8c966fb2e89e30 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_c02b59ec692640b199c2e226f35a11f3.setIcon(custom_icon_ae97b47806e343d48e8c966fb2e89e30);
        
    
            var marker_e921f03f071d49ef9709ee6b84c45469 = L.marker(
                [-19.8383441, 34.0088218],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_d4c0db49400a4253af81fa07fc69e7b9 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_e921f03f071d49ef9709ee6b84c45469.setIcon(custom_icon_d4c0db49400a4253af81fa07fc69e7b9);
        
    
            var marker_978a67c0aa1743c2bdc3259e86943b8e = L.marker(
                [-18.1932762, 35.7398222],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_f99ab3a572494e38901af123f5e13c81 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_978a67c0aa1743c2bdc3259e86943b8e.setIcon(custom_icon_f99ab3a572494e38901af123f5e13c81);
        
    
            var marker_c82e0bf31775438bb3cd9e1948948bed = L.marker(
                [-17.6664805, 35.1608594],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_07b4268616ec4cc2b0f85c6b2b79f73b = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_c82e0bf31775438bb3cd9e1948948bed.setIcon(custom_icon_07b4268616ec4cc2b0f85c6b2b79f73b);
        
    
            var marker_21eb1df6c2644f1da7ef81e48d87f502 = L.marker(
                [-17.5834422, 35.0809537],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_851f9b4d7d4f412898716df228b94b13 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_21eb1df6c2644f1da7ef81e48d87f502.setIcon(custom_icon_851f9b4d7d4f412898716df228b94b13);
        
    
            var marker_38ab9b15f2604de69a45d38896aa3ec9 = L.marker(
                [-19.5436479, 34.6257821],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_8e529f279e9c414c96912b00b10317c9 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_38ab9b15f2604de69a45d38896aa3ec9.setIcon(custom_icon_8e529f279e9c414c96912b00b10317c9);
        
    
            var marker_5641226e4353489daa036562adc4de48 = L.marker(
                [-21.0134026, 34.897447],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_148f3df02d9f42108f48927f2aa0db33 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_5641226e4353489daa036562adc4de48.setIcon(custom_icon_148f3df02d9f42108f48927f2aa0db33);
        
    
            var marker_5ab9e3af3199459aae0dcc6b9b1568e7 = L.marker(
                [-17.149661, 34.8821373],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_1e962b422b7043e3a99d42df08a3d000 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_5ab9e3af3199459aae0dcc6b9b1568e7.setIcon(custom_icon_1e962b422b7043e3a99d42df08a3d000);
        
    
            var marker_a6f2425050a34c82bbe5474d129a360a = L.marker(
                [-19.3351864, 34.3239753],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_2157fc5026174dd986d880eb97ae8fc4 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_a6f2425050a34c82bbe5474d129a360a.setIcon(custom_icon_2157fc5026174dd986d880eb97ae8fc4);
        
    
            var marker_2b896ce556614f22aa4118e580707f5a = L.marker(
                [-19.9769851, 34.1396673],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_5913f9cfe3424ae880a2e4479ebdf7cb = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_2b896ce556614f22aa4118e580707f5a.setIcon(custom_icon_5913f9cfe3424ae880a2e4479ebdf7cb);
        
    
            var marker_737b70324fac4b4aae4274abd5df5568 = L.marker(
                [-20.5759453, 33.8806591],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_3c8c97ada76b4e89880312842eda14c7 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_737b70324fac4b4aae4274abd5df5568.setIcon(custom_icon_3c8c97ada76b4e89880312842eda14c7);
        
    
            var marker_2b70e00356874ba59c02adb68f260961 = L.marker(
                [-20.6313221, 34.9039131],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_36664da28df141ed9ade15eab7659df3 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_2b70e00356874ba59c02adb68f260961.setIcon(custom_icon_36664da28df141ed9ade15eab7659df3);
        
    
            var marker_10b177d1cc4e49dbb17078ea955905c4 = L.marker(
                [-19.7884755, 34.1845044],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_eb11e34bf38240ddb89e25d8995277a9 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_10b177d1cc4e49dbb17078ea955905c4.setIcon(custom_icon_eb11e34bf38240ddb89e25d8995277a9);
        
    
            var marker_1c950421bd70485db22b2fc9232b262c = L.marker(
                [-19.3499379, 34.0635771],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_f6cdfd5a40a54b0f80a90ef98c5244e2 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_1c950421bd70485db22b2fc9232b262c.setIcon(custom_icon_f6cdfd5a40a54b0f80a90ef98c5244e2);
        
    
            var marker_9169001c832143b2bca255d69db536c5 = L.marker(
                [-16.0917146, 39.6606714],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_bccd7f78f96b488e90f0b6549e895db6 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_9169001c832143b2bca255d69db536c5.setIcon(custom_icon_bccd7f78f96b488e90f0b6549e895db6);
        
    
            var marker_07c1f3f9df0c4539909bb756f4b23365 = L.marker(
                [-14.7467462, 39.9765417],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_100e212d77814004836d91cd23529024 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_07c1f3f9df0c4539909bb756f4b23365.setIcon(custom_icon_100e212d77814004836d91cd23529024);
        
    
            var marker_82ed7854e1ec453d9f448bcf1f19d79b = L.marker(
                [-15.6010501, 38.7352771],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_615403ed8f6c481b91e52878c1ac5710 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_82ed7854e1ec453d9f448bcf1f19d79b.setIcon(custom_icon_615403ed8f6c481b91e52878c1ac5710);
        
    
            var marker_556c494df7a647848995f27b241a899e = L.marker(
                [-15.824986, 40.2255969],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_16645b15e13a426ca473550992dd4aae = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_556c494df7a647848995f27b241a899e.setIcon(custom_icon_16645b15e13a426ca473550992dd4aae);
        
    
            var marker_5ad606432c8c4b63a0094074ba7dde33 = L.marker(
                [-15.2869639, 40.1142758],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_cf229f00b2364191a773f6005ef93267 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_5ad606432c8c4b63a0094074ba7dde33.setIcon(custom_icon_cf229f00b2364191a773f6005ef93267);
        
    
            var marker_c3fbdb9998e14e2ea8fb5faaa5b88cea = L.marker(
                [-14.9830628, 36.6163574],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_d13146b1bf7948eda83c9c787ab7e477 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_c3fbdb9998e14e2ea8fb5faaa5b88cea.setIcon(custom_icon_d13146b1bf7948eda83c9c787ab7e477);
        
    
            var marker_9f75b93405cd46a39cf2f0a8ab2f13a0 = L.marker(
                [-15.1597205, 40.1979648],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_eb4eff4aef4e4019980fc274afe2a46b = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_9f75b93405cd46a39cf2f0a8ab2f13a0.setIcon(custom_icon_eb4eff4aef4e4019980fc274afe2a46b);
        
    
            var marker_ee11d154a5c1431e924201c5870c4f39 = L.marker(
                [-14.0946817, 35.4712319],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_9be121a0c4ad4d83abf5c55745ebdce5 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_ee11d154a5c1431e924201c5870c4f39.setIcon(custom_icon_9be121a0c4ad4d83abf5c55745ebdce5);
        
    
            var marker_e92516eb87454cf99cd49d327639352c = L.marker(
                [-13.0116609, 35.1868232],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_d67e21ef8a1e45ae81337a3a40288bc6 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_e92516eb87454cf99cd49d327639352c.setIcon(custom_icon_d67e21ef8a1e45ae81337a3a40288bc6);
        
    
            var marker_f0454f786ccb427fb1bbb4dc603106dc = L.marker(
                [-13.1857251, 35.1943488],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_11ddc9b1dafe4adfabbf1f812e248c3e = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_f0454f786ccb427fb1bbb4dc603106dc.setIcon(custom_icon_11ddc9b1dafe4adfabbf1f812e248c3e);
        
    
            var marker_0fff83be96f348c0a6b6f9b291156de2 = L.marker(
                [-12.7595304, 34.9763153],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_dde0ba8e8f7d42dd8d11e8543a3f41f5 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_0fff83be96f348c0a6b6f9b291156de2.setIcon(custom_icon_dde0ba8e8f7d42dd8d11e8543a3f41f5);
        
    
            var marker_9097f02d3ceb41a8b246c1a10e04d7fb = L.marker(
                [-12.8835964, 37.6889433],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ce3d22266d90460f8627b13a75b66fe9 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_9097f02d3ceb41a8b246c1a10e04d7fb.setIcon(custom_icon_ce3d22266d90460f8627b13a75b66fe9);
        
    
            var marker_a14bc1914e9a466c86d40c257c449b5c = L.marker(
                [-12.9039287, 35.0496335],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a83bd01483b4414692abd389d3ed6099 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_a14bc1914e9a466c86d40c257c449b5c.setIcon(custom_icon_a83bd01483b4414692abd389d3ed6099);
        
    
            var marker_2c0f374aaf664eadb7e052ee1f4d5a76 = L.marker(
                [-14.3765111, 35.8920363],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_f775aea2ca3c4f98a8d28247fcba861c = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_2c0f374aaf664eadb7e052ee1f4d5a76.setIcon(custom_icon_f775aea2ca3c4f98a8d28247fcba861c);
        
    
            var marker_8af7653d76d044b284b89670e41e65b2 = L.marker(
                [-14.620486, 36.3474096],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_28f5eb7bf26042cabd3e0679179f53f6 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_8af7653d76d044b284b89670e41e65b2.setIcon(custom_icon_28f5eb7bf26042cabd3e0679179f53f6);
        
    
            var marker_0203bcff80db4bd6bdc5fa1e1c0b14a3 = L.marker(
                [-14.3193925, 36.2330409],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_72affbde0af3465dbe7c71c5b5ecf06b = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_0203bcff80db4bd6bdc5fa1e1c0b14a3.setIcon(custom_icon_72affbde0af3465dbe7c71c5b5ecf06b);
        
    
            var marker_abeb1ed6672f4eabbbae879404cef1a5 = L.marker(
                [-12.8474027, 36.0650052],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_4da5f2597e1c4be3b9cf82d755907d8e = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_abeb1ed6672f4eabbbae879404cef1a5.setIcon(custom_icon_4da5f2597e1c4be3b9cf82d755907d8e);
        
    
            var marker_9b82bb609c864ab6ba61ddaa64306849 = L.marker(
                [-14.5443416, 36.6058928],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_e1bfc333187444a9a40bd6cffcb1e71b = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_9b82bb609c864ab6ba61ddaa64306849.setIcon(custom_icon_e1bfc333187444a9a40bd6cffcb1e71b);
        
    
            var marker_db53ebc2f9ff42e6ba88606e57594a05 = L.marker(
                [-13.849214, 35.2892326],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_599709fb43444ef6b212aa8eccc84298 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_db53ebc2f9ff42e6ba88606e57594a05.setIcon(custom_icon_599709fb43444ef6b212aa8eccc84298);
        
    
            var marker_68f28dc6e0cf4cf8b4a6c8be687bac2e = L.marker(
                [-15.2896146, 35.9478074],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_53f0b6bf66c64576b64ce8c081f892fe = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_68f28dc6e0cf4cf8b4a6c8be687bac2e.setIcon(custom_icon_53f0b6bf66c64576b64ce8c081f892fe);
        
    
            var marker_98940867876842449ff77fb2f28a3234 = L.marker(
                [-14.9516898, 36.164088],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_36a59aa14e5c49d5b6486be5487a7f62 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_98940867876842449ff77fb2f28a3234.setIcon(custom_icon_36a59aa14e5c49d5b6486be5487a7f62);
        
    
            var marker_ee3413c31b3445c49fcd6909d4848b31 = L.marker(
                [-12.8904834, 35.7474783],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_79e214a4f76749b4b07c0615de472f52 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_ee3413c31b3445c49fcd6909d4848b31.setIcon(custom_icon_79e214a4f76749b4b07c0615de472f52);
        
    
            var marker_f2a8669198564b6c81fb9556e49800b2 = L.marker(
                [-13.7631867, 35.3107436],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a095b3365f9e4797aaebb8c3b2a67950 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_f2a8669198564b6c81fb9556e49800b2.setIcon(custom_icon_a095b3365f9e4797aaebb8c3b2a67950);
        
    
            var marker_0728efb2275d46e197905c50555f35ea = L.marker(
                [-15.3247028, 35.9020624],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_dd4819a7d9594ccc84d49837fd3b1d45 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_0728efb2275d46e197905c50555f35ea.setIcon(custom_icon_dd4819a7d9594ccc84d49837fd3b1d45);
        
    
            var marker_25c783d60f9c4a0f9610d028e07c6f35 = L.marker(
                [-12.9780334, 35.1523226],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_3b61b56e4f514160971a6569ef068f89 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_25c783d60f9c4a0f9610d028e07c6f35.setIcon(custom_icon_3b61b56e4f514160971a6569ef068f89);
        
    
            var marker_3a1658684ad94c3d9c64905174653fb9 = L.marker(
                [-12.9490789, 35.7463869],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_42d751a3d6ab4550a13b6ee19d3d14b2 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_3a1658684ad94c3d9c64905174653fb9.setIcon(custom_icon_42d751a3d6ab4550a13b6ee19d3d14b2);
        
    
            var marker_be3d46ab8318471fb7e1d2634b11e1fe = L.marker(
                [-13.5462126, 35.4476358],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_77b0e58efef64cf887dc957d0734369d = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_be3d46ab8318471fb7e1d2634b11e1fe.setIcon(custom_icon_77b0e58efef64cf887dc957d0734369d);
        
    
            var marker_1900d414546b47128c651602bd0aaf6e = L.marker(
                [-14.7948815, 36.8536015],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_047a8e6669714e1fb42916afa1aef755 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_1900d414546b47128c651602bd0aaf6e.setIcon(custom_icon_047a8e6669714e1fb42916afa1aef755);
        
    
            var marker_4f112d3931ef41a5aa56823fdf761ef0 = L.marker(
                [-13.0897496, 35.6444181],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_e0ccad97931a4451be8e1c89c33c62c7 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_4f112d3931ef41a5aa56823fdf761ef0.setIcon(custom_icon_e0ccad97931a4451be8e1c89c33c62c7);
        
    
            var marker_f37cbc1e1099477bb8c90e48566d4641 = L.marker(
                [-12.4887609, 35.4248196],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_b014304dd31a4fc391169f5b542a2fb1 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_f37cbc1e1099477bb8c90e48566d4641.setIcon(custom_icon_b014304dd31a4fc391169f5b542a2fb1);
        
    
            var marker_c43b48d8c3e447d3a07e7a0ea8242e50 = L.marker(
                [-14.7348686, 36.4349475],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_aeaea5ff73bc488794a54d8154dde664 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_c43b48d8c3e447d3a07e7a0ea8242e50.setIcon(custom_icon_aeaea5ff73bc488794a54d8154dde664);
        
    
            var marker_f514fcde419f46ab84e18e101f95681f = L.marker(
                [-16.3513608, 36.8535839],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_800a87d951344e6abbd0b236b3913925 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_f514fcde419f46ab84e18e101f95681f.setIcon(custom_icon_800a87d951344e6abbd0b236b3913925);
        
    
            var marker_b7fef132a1414f82b1d22b2d2dcf16aa = L.marker(
                [-16.3943031, 36.9801849],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_9193ac10c0cd4986a9a32183b3b0ab51 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_b7fef132a1414f82b1d22b2d2dcf16aa.setIcon(custom_icon_9193ac10c0cd4986a9a32183b3b0ab51);
        
    
            var marker_17cd528292c74051b74ead251c7eb4f7 = L.marker(
                [-16.6595165, 34.2553563],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a45ff6827af24a27b07898562c66af17 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_17cd528292c74051b74ead251c7eb4f7.setIcon(custom_icon_a45ff6827af24a27b07898562c66af17);
        
    
            var marker_8179844644124524be59949f287a4920 = L.marker(
                [-15.9745347, 37.0442837],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a2cc218ff8ef4274a65734f55d3e7f90 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_8179844644124524be59949f287a4920.setIcon(custom_icon_a2cc218ff8ef4274a65734f55d3e7f90);
        
    
            var marker_15033da8867740838e105baa64a1edea = L.marker(
                [-17.6090419, 37.3972544],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_742b3224dcc34af790a7e8cf272db21a = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_15033da8867740838e105baa64a1edea.setIcon(custom_icon_742b3224dcc34af790a7e8cf272db21a);
        
    
            var marker_44cd5727ce664efdb47cb86a996d7eb0 = L.marker(
                [-20.2654027, 34.6690058],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_6e333fd2371a47e29af864cd9ab1dcc5 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_44cd5727ce664efdb47cb86a996d7eb0.setIcon(custom_icon_6e333fd2371a47e29af864cd9ab1dcc5);
        
    
            var marker_3e3620a2891249779986b271a4b83462 = L.marker(
                [-20.2653675, 34.6690044],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_c1bf6f81e06e44acbcdfdf1d4b157657 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_3e3620a2891249779986b271a4b83462.setIcon(custom_icon_c1bf6f81e06e44acbcdfdf1d4b157657);
        
    
            var marker_f9fe5c4966ef4328a0f82936c87d11ce = L.marker(
                [-17.5277963, 36.2963162],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a9fbe26dad0b4d7281eb1bf7f42ec940 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_f9fe5c4966ef4328a0f82936c87d11ce.setIcon(custom_icon_a9fbe26dad0b4d7281eb1bf7f42ec940);
        
    
            var marker_5d7eef112947414b894c1c01cd4e46e2 = L.marker(
                [-17.0023932, 36.7705965],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_19f939f3a9da40ddbcba8ea24558b01b = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_5d7eef112947414b894c1c01cd4e46e2.setIcon(custom_icon_19f939f3a9da40ddbcba8ea24558b01b);
        
    
            var marker_2b8cca7248fc4c64a633453493e48955 = L.marker(
                [-17.2304565, 37.7765087],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_fe6ec429268d40a9b84149c0f14df0f8 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_2b8cca7248fc4c64a633453493e48955.setIcon(custom_icon_fe6ec429268d40a9b84149c0f14df0f8);
        
    
            var marker_73c3b42bfcf6461d9ab497b656ea8d1f = L.marker(
                [-18.0780083, 36.896207],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_138eb3a252554faba6b5bcdb3e5dbdae = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_73c3b42bfcf6461d9ab497b656ea8d1f.setIcon(custom_icon_138eb3a252554faba6b5bcdb3e5dbdae);
        
    
            var marker_2699d0b99b944eddac6b181feaa032ea = L.marker(
                [-15.8630855, 37.6376085],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_4c9076d76ea74faf8ccb5ab1b2f63dd3 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_2699d0b99b944eddac6b181feaa032ea.setIcon(custom_icon_4c9076d76ea74faf8ccb5ab1b2f63dd3);
        
    
            var marker_320379b3037a4e69820d298a5ff410cd = L.marker(
                [-16.3586344, 37.7671226],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_cff4380c260e427c9d67555e408f6b17 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_320379b3037a4e69820d298a5ff410cd.setIcon(custom_icon_cff4380c260e427c9d67555e408f6b17);
        
    
            var marker_2cf7e27964e84dd69ce0442955d03aae = L.marker(
                [-17.3178065, 35.9554249],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_6fc8dcb527364314b542659a91553484 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_2cf7e27964e84dd69ce0442955d03aae.setIcon(custom_icon_6fc8dcb527364314b542659a91553484);
        
    
            var marker_54e035d1ecce4c6f8bac1e5b313f22d1 = L.marker(
                [-15.4433933, 35.9857041],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_2875b4bde45543e2b296e72dda3a760c = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_54e035d1ecce4c6f8bac1e5b313f22d1.setIcon(custom_icon_2875b4bde45543e2b296e72dda3a760c);
        
    
            var marker_a632dd44ca96442eb9408364d48e86da = L.marker(
                [-14.8010272, 36.5988113],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_37e5c2a6de304a65a47ae8002a5a92f6 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_a632dd44ca96442eb9408364d48e86da.setIcon(custom_icon_37e5c2a6de304a65a47ae8002a5a92f6);
        
    
            var marker_0d52e77dad404fd1ad3e4ac32749ec1e = L.marker(
                [-13.2889748, 35.0499447],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_2c95c090c29d4131bd11217c677c4cd8 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_0d52e77dad404fd1ad3e4ac32749ec1e.setIcon(custom_icon_2c95c090c29d4131bd11217c677c4cd8);
        
    
            var marker_a513d877f3774dcfbb267a0bf36b36fc = L.marker(
                [-14.8097363, 36.4944027],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_bfe0f650503848cfa78d56d708c15a36 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_a513d877f3774dcfbb267a0bf36b36fc.setIcon(custom_icon_bfe0f650503848cfa78d56d708c15a36);
        
    
            var marker_00890fbaf63847e3863be4734066b0dd = L.marker(
                [-14.6510364, 36.5689004],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_54414720f3234772b4a0304f735e4f37 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_00890fbaf63847e3863be4734066b0dd.setIcon(custom_icon_54414720f3234772b4a0304f735e4f37);
        
    
            var marker_4e74c38f0c984c129b446f471aa97844 = L.marker(
                [-12.6113041, 34.833084],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_f1b01d91211643afaa9a89e8a4f567c1 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_4e74c38f0c984c129b446f471aa97844.setIcon(custom_icon_f1b01d91211643afaa9a89e8a4f567c1);
        
    
            var marker_9546374bb4f449dc8d944ec47734ef7f = L.marker(
                [-13.3497149, 36.7425889],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_894b94256b8b4cad9087008bfa1f2cd5 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_9546374bb4f449dc8d944ec47734ef7f.setIcon(custom_icon_894b94256b8b4cad9087008bfa1f2cd5);
        
    
            var marker_d4f3da2df679445b80434c06487cc230 = L.marker(
                [-15.1049226, 35.957568],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_254fe0612aff4b30a4b655b583cf7e96 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_d4f3da2df679445b80434c06487cc230.setIcon(custom_icon_254fe0612aff4b30a4b655b583cf7e96);
        
    
            var marker_4d02cea0e0984a6c83ea25884eb5a457 = L.marker(
                [-13.291703, 35.4793715],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a7ea62b7f09a4273a79b69a69dc826b2 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_4d02cea0e0984a6c83ea25884eb5a457.setIcon(custom_icon_a7ea62b7f09a4273a79b69a69dc826b2);
        
    
            var marker_ccf9b4c26ae8419e8649c30caf62c282 = L.marker(
                [-15.3151093, 36.6589884],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_230bcf46b60b4a1d909309bb9f702f16 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_ccf9b4c26ae8419e8649c30caf62c282.setIcon(custom_icon_230bcf46b60b4a1d909309bb9f702f16);
        
    
            var marker_67b8def211f34443a72e206cc75dba70 = L.marker(
                [-14.4628448, 36.8949491],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_b69dfe92121e4670bfd8f1cea9855105 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_67b8def211f34443a72e206cc75dba70.setIcon(custom_icon_b69dfe92121e4670bfd8f1cea9855105);
        
    
            var marker_076467627eb14a98bf1d5468bd91be56 = L.marker(
                [-13.9300086, 37.137012],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_bfb77118723343adae7c8f544e303b0b = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_076467627eb14a98bf1d5468bd91be56.setIcon(custom_icon_bfb77118723343adae7c8f544e303b0b);
        
    
            var marker_ea223ca7bf03470d9b902de1c15d9a39 = L.marker(
                [-11.7927994, 38.0301994],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_c91f9e38af10459d919bbf140bdbbea4 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_ea223ca7bf03470d9b902de1c15d9a39.setIcon(custom_icon_c91f9e38af10459d919bbf140bdbbea4);
        
    
            var marker_8d410d8b86544937ac5e0d5d688603d0 = L.marker(
                [-14.3692334, 35.7209516],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_7a877300f5d3464d82075b247b03e731 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_8d410d8b86544937ac5e0d5d688603d0.setIcon(custom_icon_7a877300f5d3464d82075b247b03e731);
        
    
            var marker_028862d3fe7f403caa897169b25c3b66 = L.marker(
                [-13.9714238, 37.8933048],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_3d118363df9c4d7d9e577009a89157a2 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_028862d3fe7f403caa897169b25c3b66.setIcon(custom_icon_3d118363df9c4d7d9e577009a89157a2);
        
    
            var marker_c4277b9afd8f40039b204ed7f03440e4 = L.marker(
                [-14.7899614, 34.1692105],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_3e70eaae5e7d4e58a2e03dcbeaaf939f = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_c4277b9afd8f40039b204ed7f03440e4.setIcon(custom_icon_3e70eaae5e7d4e58a2e03dcbeaaf939f);
        
    
            var marker_8755a5bf2b204d90b0d67b39d20db631 = L.marker(
                [-15.2687278, 36.0015535],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_7155857e94af4247b4227390a7724e70 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_8755a5bf2b204d90b0d67b39d20db631.setIcon(custom_icon_7155857e94af4247b4227390a7724e70);
        
    
            var marker_39fe3bf4c2374b6da0be7fcc2e2705ab = L.marker(
                [-14.7804637, 36.5316144],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_d4c9e7b9356b4af0a291fb9c678f9825 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_39fe3bf4c2374b6da0be7fcc2e2705ab.setIcon(custom_icon_d4c9e7b9356b4af0a291fb9c678f9825);
        
    
            var marker_38d68026aae4461f96b85e9e342a2791 = L.marker(
                [-12.3559285, 35.3809829],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_89d4a3b94e6e41758a2fc426cabb97bf = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_38d68026aae4461f96b85e9e342a2791.setIcon(custom_icon_89d4a3b94e6e41758a2fc426cabb97bf);
        
    
            var marker_2a4d0fab0fca40a3ad7a7698f0103092 = L.marker(
                [-17.2617248, 35.6287513],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_3d82108eeccc44378035462abaf53d61 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_2a4d0fab0fca40a3ad7a7698f0103092.setIcon(custom_icon_3d82108eeccc44378035462abaf53d61);
        
    
            var marker_db03fc4fae8c4392a59a5eb825d11957 = L.marker(
                [-16.2172153, 35.6258123],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_798db1417fe0493d80ddf0d5d2d86158 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_db03fc4fae8c4392a59a5eb825d11957.setIcon(custom_icon_798db1417fe0493d80ddf0d5d2d86158);
        
    
            var marker_a19c72dfa0e3410aa09f099e9ae03064 = L.marker(
                [-15.5991452, 32.7675635],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_2fd91de0a7174490ab7981275de5667d = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_a19c72dfa0e3410aa09f099e9ae03064.setIcon(custom_icon_2fd91de0a7174490ab7981275de5667d);
        
    
            var marker_151e8b24fbe94aa5ada3cb2c253a2a57 = L.marker(
                [-17.5203911, 37.5514948],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_676934baa90f4a4c87492ac157fc80bd = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_151e8b24fbe94aa5ada3cb2c253a2a57.setIcon(custom_icon_676934baa90f4a4c87492ac157fc80bd);
        
    
            var marker_77020eb15a624be7a6dd3e92f2bf8a56 = L.marker(
                [-16.0181991, 35.9885086],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_6058c0e2dd9f46c0a871de7c68959b6e = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_77020eb15a624be7a6dd3e92f2bf8a56.setIcon(custom_icon_6058c0e2dd9f46c0a871de7c68959b6e);
        
    
            var marker_5c6931b81b204f5b98c8381693f2c015 = L.marker(
                [-16.8807322, 37.0096405],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_d95da3db249b41c08728e39ce1a17435 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_5c6931b81b204f5b98c8381693f2c015.setIcon(custom_icon_d95da3db249b41c08728e39ce1a17435);
        
    
            var marker_169d9400b99143e3a54846c9307b3e2c = L.marker(
                [-17.2668207, 38.1433075],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ae1f162e6d254fe69d3e84e672ee23f9 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_169d9400b99143e3a54846c9307b3e2c.setIcon(custom_icon_ae1f162e6d254fe69d3e84e672ee23f9);
        
    
            var marker_e63019db555240a7a81fadd4e74b1ebd = L.marker(
                [-18.2908047, 35.9453338],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_aaf2aa609c2d48b69e10eccd0525adb1 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_e63019db555240a7a81fadd4e74b1ebd.setIcon(custom_icon_aaf2aa609c2d48b69e10eccd0525adb1);
        
    
            var marker_2393e9227ab544ad90d2c68cb2f3a5bb = L.marker(
                [-18.2907518, 35.9453807],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_0001b2ab0ba54f68b7e1365021de10ed = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_2393e9227ab544ad90d2c68cb2f3a5bb.setIcon(custom_icon_0001b2ab0ba54f68b7e1365021de10ed);
        
    
            var marker_822fecf995d34496b2e34687772ede77 = L.marker(
                [-16.2102669, 35.7996977],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_dc98a074c03540948e1539831e28e95c = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_822fecf995d34496b2e34687772ede77.setIcon(custom_icon_dc98a074c03540948e1539831e28e95c);
        
    
            var marker_c698497f28094c90b5f252140a6767e3 = L.marker(
                [-17.5140636, 36.842811],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_dc84fdad69ae4c6fb557dbfacdc916db = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_c698497f28094c90b5f252140a6767e3.setIcon(custom_icon_dc84fdad69ae4c6fb557dbfacdc916db);
        
    
            var marker_ff8f4d9591f34ecfae430153e030d716 = L.marker(
                [-16.1437875, 33.6069068],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_10c65d9be4b544ad8a8940ebbe0da0d9 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_ff8f4d9591f34ecfae430153e030d716.setIcon(custom_icon_10c65d9be4b544ad8a8940ebbe0da0d9);
        
    
            var marker_00b0c5230d6e436b89391054903468fe = L.marker(
                [-15.5117552, 38.256948],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_4037233d7ca949ff9f64679e4203ef8f = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_00b0c5230d6e436b89391054903468fe.setIcon(custom_icon_4037233d7ca949ff9f64679e4203ef8f);
        
    
            var marker_2b6ff2b01646449c83a9832dae3294ba = L.marker(
                [-16.1564954, 33.5869016],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_1238be7b08da4a22bda712d21d0d57fb = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_2b6ff2b01646449c83a9832dae3294ba.setIcon(custom_icon_1238be7b08da4a22bda712d21d0d57fb);
        
    
            var marker_516c0199ae444cc8bd41da8388ed9adf = L.marker(
                [-18.2942551, 36.713676],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_c98a024a332a4dbb9b3198095f51caef = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_516c0199ae444cc8bd41da8388ed9adf.setIcon(custom_icon_c98a024a332a4dbb9b3198095f51caef);
        
    
            var marker_d6a75b459c124964998a054f512e78c4 = L.marker(
                [-17.4039242, 35.6898648],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ec21b7d18fab424f9cf1c27e4940c760 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_d6a75b459c124964998a054f512e78c4.setIcon(custom_icon_ec21b7d18fab424f9cf1c27e4940c760);
        
    
            var marker_8d07cb5034f04aebb414a51432ed2d29 = L.marker(
                [-16.6937845, 35.3493731],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_20d78777fd0e4d8da53b04f067584820 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_8d07cb5034f04aebb414a51432ed2d29.setIcon(custom_icon_20d78777fd0e4d8da53b04f067584820);
        
    
            var marker_779c37e7fa434952a88acbc9413e13e1 = L.marker(
                [-16.1321294, 38.097382],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_c80c743cabb64abb9b8d6cdb6b33cdff = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_779c37e7fa434952a88acbc9413e13e1.setIcon(custom_icon_c80c743cabb64abb9b8d6cdb6b33cdff);
        
    
            var marker_f1075bd4afe646538d3d473446107272 = L.marker(
                [-17.2409475, 35.8407383],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_0bb461e77bbd435b9093b92f23cefdaa = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_f1075bd4afe646538d3d473446107272.setIcon(custom_icon_0bb461e77bbd435b9093b92f23cefdaa);
        
    
            var marker_9344c73df6ba4a1495cd9f2134676926 = L.marker(
                [-16.3631614, 36.3790718],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_900527b323944d7e98cc56c6de2ebbb6 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_9344c73df6ba4a1495cd9f2134676926.setIcon(custom_icon_900527b323944d7e98cc56c6de2ebbb6);
        
    
            var marker_81fb05cd90b245b9973a9e0e52311369 = L.marker(
                [-18.1113728, 36.7580786],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_c43a9947bdc54f7db40fe80b47f11e55 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_81fb05cd90b245b9973a9e0e52311369.setIcon(custom_icon_c43a9947bdc54f7db40fe80b47f11e55);
        
    
            var marker_8098dfd39eaf4712bb56e77f229008b4 = L.marker(
                [-16.0564282, 36.0288497],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_31cdaa56b52748839eb8b05b4d1752d3 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_8098dfd39eaf4712bb56e77f229008b4.setIcon(custom_icon_31cdaa56b52748839eb8b05b4d1752d3);
        
    
            var marker_d2c0702a93df429dbf5238344c844528 = L.marker(
                [-17.4293899, 37.5695716],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_6f80c826f1394697b3599c2f0e06b5f5 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_d2c0702a93df429dbf5238344c844528.setIcon(custom_icon_6f80c826f1394697b3599c2f0e06b5f5);
        
    
            var marker_e16e255869e04957b2c4a857d4345495 = L.marker(
                [-14.9869947, 34.332325],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_c542292a00b247a4a98518daaef2e83d = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_e16e255869e04957b2c4a857d4345495.setIcon(custom_icon_c542292a00b247a4a98518daaef2e83d);
        
    
            var marker_92026fe276bc4a4b800b2d54bf64b9c3 = L.marker(
                [-17.1638246, 34.8887251],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_d5b180707d8646f0a7a0c7091897507b = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_92026fe276bc4a4b800b2d54bf64b9c3.setIcon(custom_icon_d5b180707d8646f0a7a0c7091897507b);
        
    
            var marker_9935af64bc774c9f9b86392940d27f19 = L.marker(
                [-14.9034688, 33.6119306],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_8af8e4dff8a44bafb15eccaa9cc2e577 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_9935af64bc774c9f9b86392940d27f19.setIcon(custom_icon_8af8e4dff8a44bafb15eccaa9cc2e577);
        
    
            var marker_a4e3ac56bf1942599bb65fa16052fa7e = L.marker(
                [-20.1162139, 33.7821557],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_273d269bd055487fa67a0457bd7a2d1c = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_a4e3ac56bf1942599bb65fa16052fa7e.setIcon(custom_icon_273d269bd055487fa67a0457bd7a2d1c);
        
    
            var marker_bb95990d2d404875b4a5cce3d66062d2 = L.marker(
                [-18.5832634, 36.4643043],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_315bec146af84cbf9c86a2c1a64fb751 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_bb95990d2d404875b4a5cce3d66062d2.setIcon(custom_icon_315bec146af84cbf9c86a2c1a64fb751);
        
    
            var marker_ff58ee63dc1b4264b8129c5a3ee0e310 = L.marker(
                [-15.768402, 36.0217486],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ece7ccbe0dc24d608ec63086f98bac13 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_ff58ee63dc1b4264b8129c5a3ee0e310.setIcon(custom_icon_ece7ccbe0dc24d608ec63086f98bac13);
        
    
            var marker_69bd89cd0cf4469ba6ff96e8d6a464e2 = L.marker(
                [-20.3270406, 33.8855052],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_f847da1929794fe48b7292afd7292a19 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_69bd89cd0cf4469ba6ff96e8d6a464e2.setIcon(custom_icon_f847da1929794fe48b7292afd7292a19);
        
    
            var marker_29ac3a98d32a455c819878f06e81dc0c = L.marker(
                [-17.2079052, 37.3132436],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_edebd5b98dbc4712bb3394e7fdb6221f = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_29ac3a98d32a455c819878f06e81dc0c.setIcon(custom_icon_edebd5b98dbc4712bb3394e7fdb6221f);
        
    
            var marker_092b24f6c474482fa95ba5305da94a17 = L.marker(
                [-16.16823, 35.4533744],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_c27e8c0c8f0043209a408da0a4f36e3c = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_092b24f6c474482fa95ba5305da94a17.setIcon(custom_icon_c27e8c0c8f0043209a408da0a4f36e3c);
        
    
            var marker_5b1bfedcebf645fd991ae188ca1f3aa4 = L.marker(
                [-14.7205362, 34.360971],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_c8c267e479814643881026c54f21f8a2 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_5b1bfedcebf645fd991ae188ca1f3aa4.setIcon(custom_icon_c8c267e479814643881026c54f21f8a2);
        
    
            var marker_d76ff717b1744cd8b4eb367ffc686bd1 = L.marker(
                [-16.2175154, 37.001017],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_595bba9d32ac4ca8a9d2b3342d116eff = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_d76ff717b1744cd8b4eb367ffc686bd1.setIcon(custom_icon_595bba9d32ac4ca8a9d2b3342d116eff);
        
    
            var marker_24c4f2ac54e04469941f48ee047cfb69 = L.marker(
                [-16.1725623, 34.2631381],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_c2add1b6dd4544e0a19d5c49cdce9437 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_24c4f2ac54e04469941f48ee047cfb69.setIcon(custom_icon_c2add1b6dd4544e0a19d5c49cdce9437);
        
    
            var marker_4ae640642f0d45a6b2378edff648384c = L.marker(
                [-15.2866321, 36.3508241],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_9685a2743afc4f09a78ed07198a85724 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_4ae640642f0d45a6b2378edff648384c.setIcon(custom_icon_9685a2743afc4f09a78ed07198a85724);
        
    
            var marker_3379204802704472b109674a6bdaf61f = L.marker(
                [-14.3324567, 36.7967172],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_791d4fce0090400288cf377e31f2de29 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_3379204802704472b109674a6bdaf61f.setIcon(custom_icon_791d4fce0090400288cf377e31f2de29);
        
    
            var marker_6980fb2e3a9d48d5925d403eca3e6485 = L.marker(
                [-12.0129822, 34.9015843],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_e7637a6302cb43f3ac617ad283ad6bc4 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_6980fb2e3a9d48d5925d403eca3e6485.setIcon(custom_icon_e7637a6302cb43f3ac617ad283ad6bc4);
        
    
            var marker_8fabdf66129047cda4bf0c5bd9e5fee6 = L.marker(
                [-13.189393, 37.50579],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_42127a9d92894ddf86ef5998e2ca01dc = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_8fabdf66129047cda4bf0c5bd9e5fee6.setIcon(custom_icon_42127a9d92894ddf86ef5998e2ca01dc);
        
    
            var marker_274c76ec943c4dc3b40a7c1a113b8b22 = L.marker(
                [-12.1964894, 38.0148619],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_cb6985ec79c0439dae3bb71a6ac8a44f = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_274c76ec943c4dc3b40a7c1a113b8b22.setIcon(custom_icon_cb6985ec79c0439dae3bb71a6ac8a44f);
        
    
            var marker_8e52068b925f4798bc42b4aa6fd8edaf = L.marker(
                [-12.5672884, 36.2640177],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_5edfad5448a8432e93207d668fbe5384 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_8e52068b925f4798bc42b4aa6fd8edaf.setIcon(custom_icon_5edfad5448a8432e93207d668fbe5384);
        
    
            var marker_49b18cf54b49457389e813e0cc92ae6c = L.marker(
                [-13.4756407, 36.1209849],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ec29ee539eb54eecb23fa9ca9c5bb33d = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_49b18cf54b49457389e813e0cc92ae6c.setIcon(custom_icon_ec29ee539eb54eecb23fa9ca9c5bb33d);
        
    
            var marker_d523e0aeaa5047fc992c6f8b21c78a82 = L.marker(
                [-12.8860268, 34.7724024],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_65af6d03cfda40de8d098f236eefd3c6 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_d523e0aeaa5047fc992c6f8b21c78a82.setIcon(custom_icon_65af6d03cfda40de8d098f236eefd3c6);
        
    
            var marker_ab1a5fd58bb84f02b8dae2f34e4ed8a4 = L.marker(
                [-20.4979563, 33.6159868],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_51b33948cd024f6c9b780504b9ec2128 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_ab1a5fd58bb84f02b8dae2f34e4ed8a4.setIcon(custom_icon_51b33948cd024f6c9b780504b9ec2128);
        
    
            var marker_a33cd0c04cf04311ab3b8355abb06ac1 = L.marker(
                [-14.218042, 36.9199687],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_6fa66b1da1de41de8faaffd264d0acaa = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_a33cd0c04cf04311ab3b8355abb06ac1.setIcon(custom_icon_6fa66b1da1de41de8faaffd264d0acaa);
        
    
            var marker_4e709d70de5b4fb2907047ebb5441c7b = L.marker(
                [-12.8776336, 35.4114836],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_9d7d19daeabb458d88b540b78bca7dc3 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_4e709d70de5b4fb2907047ebb5441c7b.setIcon(custom_icon_9d7d19daeabb458d88b540b78bca7dc3);
        
    
            var marker_5f76e2ff8bae43c48f5f5668fd183b7e = L.marker(
                [-19.2454385, 34.0354528],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_8ef2f0fa36ba471db87523316e6dd38a = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_5f76e2ff8bae43c48f5f5668fd183b7e.setIcon(custom_icon_8ef2f0fa36ba471db87523316e6dd38a);
        
    
            var marker_c984b58ef00a437699c55d78d0114b9b = L.marker(
                [-14.7293128, 36.62692],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_3ecc510cb0784cab8eae5a537b33e9f3 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_c984b58ef00a437699c55d78d0114b9b.setIcon(custom_icon_3ecc510cb0784cab8eae5a537b33e9f3);
        
    
            var marker_e6f1b6bef2a74525b41423d31215cdd8 = L.marker(
                [-13.1900667, 37.5050765],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_9dc183d599974772b06998a4094e7159 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_e6f1b6bef2a74525b41423d31215cdd8.setIcon(custom_icon_9dc183d599974772b06998a4094e7159);
        
    
            var marker_7c9bb3c0cf8347c3b89c7cbdb8c9ad8a = L.marker(
                [-14.1269525, 35.937098],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_07d370e238934b6195aa8251c9450a09 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_7c9bb3c0cf8347c3b89c7cbdb8c9ad8a.setIcon(custom_icon_07d370e238934b6195aa8251c9450a09);
        
    
            var marker_46d20398428745bb908544040d81737f = L.marker(
                [-12.2773372, 37.6608659],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_3122a9fb50d641bb93f8b8f9b9014c85 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_46d20398428745bb908544040d81737f.setIcon(custom_icon_3122a9fb50d641bb93f8b8f9b9014c85);
        
    
            var marker_577e9a37ef884a35b13c85556e27214f = L.marker(
                [-12.1164273, 37.6657254],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_5b7ae50ad2c74467b37e70942e25594a = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_577e9a37ef884a35b13c85556e27214f.setIcon(custom_icon_5b7ae50ad2c74467b37e70942e25594a);
        
    
            var marker_e052f5982bdb4285a79ecc457ce779a7 = L.marker(
                [-14.322402, 36.7909585],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_4776bb2def23498e867ea0e9b24c21ca = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_e052f5982bdb4285a79ecc457ce779a7.setIcon(custom_icon_4776bb2def23498e867ea0e9b24c21ca);
        
    
            var marker_b1e65a6109db430795c57254fc0a7f56 = L.marker(
                [-14.0323409, 37.8555085],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_46f90f85d69f4fc9b99af79cd60fd9ab = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_b1e65a6109db430795c57254fc0a7f56.setIcon(custom_icon_46f90f85d69f4fc9b99af79cd60fd9ab);
        
    
            var marker_1792ef7edeaa45c0be090347e385e20b = L.marker(
                [-19.4069613, 34.4372571],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_0270549b2b9147b291dd2c9bf689e9a8 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_1792ef7edeaa45c0be090347e385e20b.setIcon(custom_icon_0270549b2b9147b291dd2c9bf689e9a8);
        
    
            var marker_8a2fedec14084d4a94a7a022cb745377 = L.marker(
                [-14.3201507, 36.792537],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_2a1a9fb655c14865aa5d2be35e14943c = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_8a2fedec14084d4a94a7a022cb745377.setIcon(custom_icon_2a1a9fb655c14865aa5d2be35e14943c);
        
    
            var marker_77a78da085ac413e833b82c2fa790c6c = L.marker(
                [-14.1332509, 38.3081574],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_e119bf484a7844c4ae14ff71e17a9c2a = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_77a78da085ac413e833b82c2fa790c6c.setIcon(custom_icon_e119bf484a7844c4ae14ff71e17a9c2a);
        
    
            var marker_df4e74dba34046e1b48de8d48eb26935 = L.marker(
                [-12.9452673, 35.4264759],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_6c4a35f6ea204248aabd4fbe6e71af77 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_df4e74dba34046e1b48de8d48eb26935.setIcon(custom_icon_6c4a35f6ea204248aabd4fbe6e71af77);
        
    
            var marker_19344eca34af40d18f2b9035543d436e = L.marker(
                [-20.3587109, 34.6342874],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_66141bf0ef2340a48eee23c60e9d05d9 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_19344eca34af40d18f2b9035543d436e.setIcon(custom_icon_66141bf0ef2340a48eee23c60e9d05d9);
        
    
            var marker_fc3ee3f84f404afc983ab79628950c44 = L.marker(
                [-15.3271816, 36.1317466],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_4889e1e7a7ad499c9e2a94946e5a6bba = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_fc3ee3f84f404afc983ab79628950c44.setIcon(custom_icon_4889e1e7a7ad499c9e2a94946e5a6bba);
        
    
            var marker_91fd1eb6663742f89a65fdf4adcd8b1c = L.marker(
                [-13.4745523, 35.2805898],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_0b496fcb48c7449cb993317537146286 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_91fd1eb6663742f89a65fdf4adcd8b1c.setIcon(custom_icon_0b496fcb48c7449cb993317537146286);
        
    
            var marker_57f1ec243fb64559bc317954738baad2 = L.marker(
                [-13.0853938, 35.6418807],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_9401bf8af67e4d76a4396a7478c5d55e = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_57f1ec243fb64559bc317954738baad2.setIcon(custom_icon_9401bf8af67e4d76a4396a7478c5d55e);
        
    
            var marker_8d9374ac70a34e9885ca2212e192f2ff = L.marker(
                [-20.8222023, 34.8527755],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a57ab39f7a744027b0671d9955c08d69 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_8d9374ac70a34e9885ca2212e192f2ff.setIcon(custom_icon_a57ab39f7a744027b0671d9955c08d69);
        
    
            var marker_10d3e8fe0ce645e98c1ec495361d384d = L.marker(
                [-14.1452771, 35.4812922],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_d6e299f9ddd74684aa610a5a77f830fb = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_10d3e8fe0ce645e98c1ec495361d384d.setIcon(custom_icon_d6e299f9ddd74684aa610a5a77f830fb);
        
    
            var marker_3d35841b67cd4a94835d8d8e66bb3896 = L.marker(
                [-13.7903033, 37.936072],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_168c37497f3942559afb99996fa8565b = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_3d35841b67cd4a94835d8d8e66bb3896.setIcon(custom_icon_168c37497f3942559afb99996fa8565b);
        
    
            var marker_003384abc1284342b4e965ed29f4be11 = L.marker(
                [-13.0905869, 37.5982927],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_85595b38b2944bd09b5d407117b4494f = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_003384abc1284342b4e965ed29f4be11.setIcon(custom_icon_85595b38b2944bd09b5d407117b4494f);
        
    
            var marker_cba001b54558474d90b596efd6dd2f8e = L.marker(
                [-14.3537827, 35.6484635],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_d846e7a379bb4afba320b3304672034c = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_cba001b54558474d90b596efd6dd2f8e.setIcon(custom_icon_d846e7a379bb4afba320b3304672034c);
        
    
            var marker_f5b32d0dbcbc48bb8402e08d6f888402 = L.marker(
                [-14.8011987, 36.5333618],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_c048057a47bc4cbd9ed2b3741f5e77ae = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_f5b32d0dbcbc48bb8402e08d6f888402.setIcon(custom_icon_c048057a47bc4cbd9ed2b3741f5e77ae);
        
    
            var marker_0c0dcf0c3bea40a4875b06e80b2ed458 = L.marker(
                [-20.3199212, 34.0559354],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_4559df1d19194787816db3ef0ade23ea = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_0c0dcf0c3bea40a4875b06e80b2ed458.setIcon(custom_icon_4559df1d19194787816db3ef0ade23ea);
        
    
            var marker_e5d043f7eff346f58d409c29db85f0b6 = L.marker(
                [-13.8769949, 37.1612026],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_512302ecf61547be9c8ac85f78c4ac8c = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_e5d043f7eff346f58d409c29db85f0b6.setIcon(custom_icon_512302ecf61547be9c8ac85f78c4ac8c);
        
    
            var marker_9e47cf3b2f934ee8861a1d0488730647 = L.marker(
                [-13.5040473, 36.4389125],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_7f6158365a6f4402b60522c5abd8c717 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_9e47cf3b2f934ee8861a1d0488730647.setIcon(custom_icon_7f6158365a6f4402b60522c5abd8c717);
        
    
            var marker_5caea445e9f348798fc214d09b87696b = L.marker(
                [-14.1597317, 37.4463147],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_b758aef6692947349d5ebb84ecdf732b = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_5caea445e9f348798fc214d09b87696b.setIcon(custom_icon_b758aef6692947349d5ebb84ecdf732b);
        
    
            var marker_0a95878ba32742b3b77afc24d6e0dfdc = L.marker(
                [-12.6129999, 34.7911987],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_7902d3b687fd42b4a378d589acff11d8 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_0a95878ba32742b3b77afc24d6e0dfdc.setIcon(custom_icon_7902d3b687fd42b4a378d589acff11d8);
        
    
            var marker_deaf70af8ee341acbeb612ce052b2ad0 = L.marker(
                [-13.8681609, 37.1597783],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_f0dd515983a04a42942a171c4b39ce5f = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_deaf70af8ee341acbeb612ce052b2ad0.setIcon(custom_icon_f0dd515983a04a42942a171c4b39ce5f);
        
    
            var marker_0aedcdf396bd47a39d2bb375b04501bf = L.marker(
                [-11.3389909, 38.3065709],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_40e09181fe4745cab088a11cdc5fd8be = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_0aedcdf396bd47a39d2bb375b04501bf.setIcon(custom_icon_40e09181fe4745cab088a11cdc5fd8be);
        
    
            var marker_fd2f84eb1b544c998ee28e6975142985 = L.marker(
                [-13.3542792, 35.420687],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_fe702ccac1ca467b8fd84ba6c30d29b7 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_fd2f84eb1b544c998ee28e6975142985.setIcon(custom_icon_fe702ccac1ca467b8fd84ba6c30d29b7);
        
    
            var marker_71689a8a006f4ee0a092ab1814b9e3ce = L.marker(
                [-12.0736621, 37.016427],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_8f27cb7d321d4c41b4b3d61aff6cd104 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_71689a8a006f4ee0a092ab1814b9e3ce.setIcon(custom_icon_8f27cb7d321d4c41b4b3d61aff6cd104);
        
    
            var marker_09629579263841d495d2af1e728577f2 = L.marker(
                [-14.6927937, 36.9643325],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_c34deee1613c4a23b2740d1ec5678fcc = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_09629579263841d495d2af1e728577f2.setIcon(custom_icon_c34deee1613c4a23b2740d1ec5678fcc);
        
    
            var marker_e95182edb58d48d7b95277d731687cb2 = L.marker(
                [-14.0319285, 37.8552926],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_63f8b4b9cac54283873058626e76e90f = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_e95182edb58d48d7b95277d731687cb2.setIcon(custom_icon_63f8b4b9cac54283873058626e76e90f);
        
    
            var marker_e72e769ae4dc4521b511ff61c5eba3bb = L.marker(
                [-14.031784, 37.8546435],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ef68894a174c4277bb41d5f987b07635 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_e72e769ae4dc4521b511ff61c5eba3bb.setIcon(custom_icon_ef68894a174c4277bb41d5f987b07635);
        
    
            var marker_df08e7a247fa4b76950cda80fce82f33 = L.marker(
                [-13.9007538, 35.4377975],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_9a066b53413a48b985917eb95238a498 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_df08e7a247fa4b76950cda80fce82f33.setIcon(custom_icon_9a066b53413a48b985917eb95238a498);
        
    
            var marker_0296aac7bbe840eb9f8330c48570efa6 = L.marker(
                [-14.799974, 36.5337816],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_5bcef211283648daa454ba213a02adf2 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_0296aac7bbe840eb9f8330c48570efa6.setIcon(custom_icon_5bcef211283648daa454ba213a02adf2);
        
    
            var marker_30369546418e4f8a85da432ce37f6c06 = L.marker(
                [-15.030027, 36.0266268],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_7ce3f8d267264fbda63c9a7057dc44c2 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_30369546418e4f8a85da432ce37f6c06.setIcon(custom_icon_7ce3f8d267264fbda63c9a7057dc44c2);
        
    
            var marker_f1c86043a6884af5bfcd4dedbb541efb = L.marker(
                [-12.1431259, 37.6719207],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_f509833ce56a4041b44b3d96864615ab = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_f1c86043a6884af5bfcd4dedbb541efb.setIcon(custom_icon_f509833ce56a4041b44b3d96864615ab);
        
    
            var marker_2747941cf54f41fe8fb1be41c58f6eac = L.marker(
                [-11.6156086, 34.9613238],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_8eeb770824e54569afc6d36ce1b09f5a = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_2747941cf54f41fe8fb1be41c58f6eac.setIcon(custom_icon_8eeb770824e54569afc6d36ce1b09f5a);
        
    
            var marker_7e503f811be84fe2a1df5c4b2eac6524 = L.marker(
                [-14.0309669, 37.8531978],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_7eddf710e42e46228249fba009530a16 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_7e503f811be84fe2a1df5c4b2eac6524.setIcon(custom_icon_7eddf710e42e46228249fba009530a16);
        
    
            var marker_7df47a0af9e1406bb84cd4846bf73a5e = L.marker(
                [-15.2848501, 37.439864],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ec18ee1f3579466bb984e55f05232ac1 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_7df47a0af9e1406bb84cd4846bf73a5e.setIcon(custom_icon_ec18ee1f3579466bb984e55f05232ac1);
        
    
            var marker_4222a13b95d84e64a29d3dbdfb93705c = L.marker(
                [-16.0360475, 37.5237883],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_5d51122a998f439f82f8f4809e601a82 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_4222a13b95d84e64a29d3dbdfb93705c.setIcon(custom_icon_5d51122a998f439f82f8f4809e601a82);
        
    
            var marker_5976ebc2d3bf4e5d94f1f4a78ad076ba = L.marker(
                [-15.9625605, 38.4414464],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_9ab1fce6da80407fb7fe3dddd503aad9 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_5976ebc2d3bf4e5d94f1f4a78ad076ba.setIcon(custom_icon_9ab1fce6da80407fb7fe3dddd503aad9);
        
    
            var marker_cb708fc14e3c4927b232fb5e48d41045 = L.marker(
                [-16.8944395, 38.2917758],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_1a21baaaeca3498b91e7ffddbffc1f75 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_cb708fc14e3c4927b232fb5e48d41045.setIcon(custom_icon_1a21baaaeca3498b91e7ffddbffc1f75);
        
    
            var marker_944be93bea624841a1c7a007d7fde444 = L.marker(
                [-15.4337374, 37.4432409],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_91a571ec7ad6436798f84d7072c2552c = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_944be93bea624841a1c7a007d7fde444.setIcon(custom_icon_91a571ec7ad6436798f84d7072c2552c);
        
    
            var marker_cf868cd356e144e2a306e60cb51246ad = L.marker(
                [-17.7309853, 37.0756897],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_9ebab571c7224a55ac04902ce4740f25 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_cf868cd356e144e2a306e60cb51246ad.setIcon(custom_icon_9ebab571c7224a55ac04902ce4740f25);
        
    
            var marker_b409a021fa6c4aab9b12c2504146f0f3 = L.marker(
                [-15.5403179, 36.8841646],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_1852bbee63774494aa9dd2020d456771 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_b409a021fa6c4aab9b12c2504146f0f3.setIcon(custom_icon_1852bbee63774494aa9dd2020d456771);
        
    
            var marker_408e3c6ced344bb5a7dbf765567bba33 = L.marker(
                [-17.1468039, 36.9371436],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_e326e199283745489a65f0912d72d75c = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_408e3c6ced344bb5a7dbf765567bba33.setIcon(custom_icon_e326e199283745489a65f0912d72d75c);
        
    
            var marker_fb17bea8ad274a33b6298c7db97d1146 = L.marker(
                [-17.3589843, 35.3535721],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_565140cae2804f5b8f434ca9a331fc79 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_fb17bea8ad274a33b6298c7db97d1146.setIcon(custom_icon_565140cae2804f5b8f434ca9a331fc79);
        
    
            var marker_f72d025d04d14c63a7b254c34c0543a7 = L.marker(
                [-17.7155627, 37.1926099],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_20236f94c7c94ebd8bccf2f0729dd887 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_f72d025d04d14c63a7b254c34c0543a7.setIcon(custom_icon_20236f94c7c94ebd8bccf2f0729dd887);
        
    
            var marker_e638664639b4499fa443b0c69e748d66 = L.marker(
                [-16.115031, 37.0792745],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_aad4e3bbc39d465bb95fcdf0cdb451e1 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_e638664639b4499fa443b0c69e748d66.setIcon(custom_icon_aad4e3bbc39d465bb95fcdf0cdb451e1);
        
    
            var marker_8a6a5d1db2924c39a3f11c33369f2bec = L.marker(
                [-18.3676548, 36.5683325],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_dbe177153cd04e6b8c9aaf31dc440d7f = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_8a6a5d1db2924c39a3f11c33369f2bec.setIcon(custom_icon_dbe177153cd04e6b8c9aaf31dc440d7f);
        
    
            var marker_52792c2fecee4cc8bae20cc47ff038a1 = L.marker(
                [-17.5811224, 36.6956194],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a8b32750461f4e87b41d89a943594ec5 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_52792c2fecee4cc8bae20cc47ff038a1.setIcon(custom_icon_a8b32750461f4e87b41d89a943594ec5);
        
    
            var marker_c7db9f8ad8854f56b1374811f8a54cd8 = L.marker(
                [-16.0178375, 36.4856923],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ac42855efcdb4ac0ae82544ab13025f9 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_c7db9f8ad8854f56b1374811f8a54cd8.setIcon(custom_icon_ac42855efcdb4ac0ae82544ab13025f9);
        
    
            var marker_02707ed7c25144f49748d46a28f737c1 = L.marker(
                [-15.9538498, 36.8659376],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_4ecf1e191b4144cbb2005f2e4544f9f0 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_02707ed7c25144f49748d46a28f737c1.setIcon(custom_icon_4ecf1e191b4144cbb2005f2e4544f9f0);
        
    
            var marker_17c72ca387454fd598c81c6ff830e511 = L.marker(
                [-17.9798199, 35.7150963],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_0f62d152979b4b2bb77fb2bedede7d22 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_17c72ca387454fd598c81c6ff830e511.setIcon(custom_icon_0f62d152979b4b2bb77fb2bedede7d22);
        
    
            var marker_e02612b180904436a0915ea3997f8366 = L.marker(
                [-15.4870032, 36.2712295],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_e363271b88284c7f85353fccf6564efb = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_e02612b180904436a0915ea3997f8366.setIcon(custom_icon_e363271b88284c7f85353fccf6564efb);
        
    
            var marker_d2097a61d85441878091ed32a4b6dbba = L.marker(
                [-16.5928109, 36.9722047],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_18bbab2107b04e02bd321b9fdf2d4704 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_d2097a61d85441878091ed32a4b6dbba.setIcon(custom_icon_18bbab2107b04e02bd321b9fdf2d4704);
        
    
            var marker_dc27c0af440a451cb47be303af91ddde = L.marker(
                [-16.8388866, 36.9800596],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_3768cfd151d04594bf48804e39c60959 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_dc27c0af440a451cb47be303af91ddde.setIcon(custom_icon_3768cfd151d04594bf48804e39c60959);
        
    
            var marker_3e84e59ece5d4a9eb4438b15308d6033 = L.marker(
                [-15.5126172, 38.2577339],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_86cb2023fa694583b9565f86db0f4a23 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_3e84e59ece5d4a9eb4438b15308d6033.setIcon(custom_icon_86cb2023fa694583b9565f86db0f4a23);
        
    
            var marker_95150d58a82349cdbf5aa634e76cf69e = L.marker(
                [-16.0700805, 37.3649995],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_811e428670c3472f96313b03d0ab05a3 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_95150d58a82349cdbf5aa634e76cf69e.setIcon(custom_icon_811e428670c3472f96313b03d0ab05a3);
        
    
            var marker_a1d4ee3ac11d42a5934300b77310c465 = L.marker(
                [-15.8714241, 37.0222179],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_7998b165f35144c3a0f5a024ade86d87 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_a1d4ee3ac11d42a5934300b77310c465.setIcon(custom_icon_7998b165f35144c3a0f5a024ade86d87);
        
    
            var marker_8e40688eb4dc4b79a890b32070bc3090 = L.marker(
                [-17.5342134, 35.6244229],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_719418203df0435cbbb81686c80454e4 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_8e40688eb4dc4b79a890b32070bc3090.setIcon(custom_icon_719418203df0435cbbb81686c80454e4);
        
    
            var marker_4ccf0f48784843a798767b82e1f6e38b = L.marker(
                [-17.6354789, 37.121642],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a0ba3444bccd4f44b98f764ff488d2da = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_4ccf0f48784843a798767b82e1f6e38b.setIcon(custom_icon_a0ba3444bccd4f44b98f764ff488d2da);
        
    
            var marker_01c145b5765045bba468f02d56e5d6ad = L.marker(
                [-17.438356, 37.2857302],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_37d348eeeea34f6cab8c8b6d3f1e97ab = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_01c145b5765045bba468f02d56e5d6ad.setIcon(custom_icon_37d348eeeea34f6cab8c8b6d3f1e97ab);
        
    
            var marker_9c373700493c41e7a0109d087c8acd18 = L.marker(
                [-16.4383786, 35.4995466],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_9dea82ecb0c24c0e9f539813738a7443 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_9c373700493c41e7a0109d087c8acd18.setIcon(custom_icon_9dea82ecb0c24c0e9f539813738a7443);
        
    
            var marker_be13f05105e1495195006262102b4a1c = L.marker(
                [-16.2184393, 36.9361585],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_d1121766e415486291b7861fdbdb2279 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_be13f05105e1495195006262102b4a1c.setIcon(custom_icon_d1121766e415486291b7861fdbdb2279);
        
    
            var marker_c17f947702384d90a4dd34c03d14d357 = L.marker(
                [-17.6399694, 37.2716291],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_00978736e2774f1d8967337f471c9cc4 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_c17f947702384d90a4dd34c03d14d357.setIcon(custom_icon_00978736e2774f1d8967337f471c9cc4);
        
    
            var marker_53e368f2312a4b178170ea0e457d2ce3 = L.marker(
                [-16.0883057, 36.9593271],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_2f322f68bb14441787bac785702fdb9d = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_53e368f2312a4b178170ea0e457d2ce3.setIcon(custom_icon_2f322f68bb14441787bac785702fdb9d);
        
    
            var marker_4a7b766e91594d10a327dd1fc0c2ff23 = L.marker(
                [-15.9805435, 38.3319895],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_09e45d6095684f47a3c7dfbb7f41bc5a = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_4a7b766e91594d10a327dd1fc0c2ff23.setIcon(custom_icon_09e45d6095684f47a3c7dfbb7f41bc5a);
        
    
            var marker_0f2be56c998b4179b251ffd745d86869 = L.marker(
                [-17.7854542, 36.9068353],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_4813db5839694180b6192cb4c20af205 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_0f2be56c998b4179b251ffd745d86869.setIcon(custom_icon_4813db5839694180b6192cb4c20af205);
        
    
            var marker_f06cf9a411054c12a9e66941fd7d2d76 = L.marker(
                [-16.0985519, 35.7691525],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_2b9f53b5ba4f40bb92253ef960d2ca11 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_f06cf9a411054c12a9e66941fd7d2d76.setIcon(custom_icon_2b9f53b5ba4f40bb92253ef960d2ca11);
        
    
            var marker_ef33a74575424e81a934c183295c9dd9 = L.marker(
                [-15.6701112, 37.5733609],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_e9a86f1bd97a4b89a36cc41fbaa3d5d1 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_ef33a74575424e81a934c183295c9dd9.setIcon(custom_icon_e9a86f1bd97a4b89a36cc41fbaa3d5d1);
        
    
            var marker_8b336f0026504ab9a2278ac86e10e5c6 = L.marker(
                [-15.9180563, 37.8524226],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_bcf833f4fa1e4fff81976d5b98a47d1e = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_8b336f0026504ab9a2278ac86e10e5c6.setIcon(custom_icon_bcf833f4fa1e4fff81976d5b98a47d1e);
        
    
            var marker_b9372c326362478c8c73504353bd130d = L.marker(
                [-16.692101, 37.371302],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_7d7c5ddb174c4227a23252bf405be862 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_b9372c326362478c8c73504353bd130d.setIcon(custom_icon_7d7c5ddb174c4227a23252bf405be862);
        
    
            var marker_767516ae5ade4bdeb62279f0162433d8 = L.marker(
                [-17.4093764, 37.1191791],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_cb51b46411814457bc8788cd8d120634 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_767516ae5ade4bdeb62279f0162433d8.setIcon(custom_icon_cb51b46411814457bc8788cd8d120634);
        
    
            var marker_8690016ae2de4e3d81532d77b5102400 = L.marker(
                [-15.1720914, 36.8049311],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_678cf1ad2884468fb948083c5ac46488 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_8690016ae2de4e3d81532d77b5102400.setIcon(custom_icon_678cf1ad2884468fb948083c5ac46488);
        
    
            var marker_d988f703a64c440781bb7bbb188e1501 = L.marker(
                [-17.2280198, 37.0246141],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_2e9c207743a9476795aa8eccb02c60d8 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_d988f703a64c440781bb7bbb188e1501.setIcon(custom_icon_2e9c207743a9476795aa8eccb02c60d8);
        
    
            var marker_5a65584aad08460fb206c208c7704222 = L.marker(
                [-16.9928455, 38.4815924],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_e3705d28f0c1455d8355e90c3f0121d9 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_5a65584aad08460fb206c208c7704222.setIcon(custom_icon_e3705d28f0c1455d8355e90c3f0121d9);
        
    
            var marker_533d33c4d34340abb5e088a939d28df0 = L.marker(
                [-17.3278278, 35.5768787],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_29774a78123047ea9a3cad72b5967c6b = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_533d33c4d34340abb5e088a939d28df0.setIcon(custom_icon_29774a78123047ea9a3cad72b5967c6b);
        
    
            var marker_d22ab6b4807c4bd4b1df029fa6ccc367 = L.marker(
                [-17.27437, 38.1781105],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_d19508251c3b43feb4997464d71f6669 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_d22ab6b4807c4bd4b1df029fa6ccc367.setIcon(custom_icon_d19508251c3b43feb4997464d71f6669);
        
    
            var marker_8a260b1ce2e645499b9e2581b1a1530d = L.marker(
                [-17.7635554, 36.323426],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_e48d231f05354fe092992bae6b37905e = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_8a260b1ce2e645499b9e2581b1a1530d.setIcon(custom_icon_e48d231f05354fe092992bae6b37905e);
        
    
            var marker_b624fe7bb1214c68a4d8e1eb845387c1 = L.marker(
                [-17.099462, 35.7259921],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_8cad53f2372f4d91b4d70834886e7d88 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_b624fe7bb1214c68a4d8e1eb845387c1.setIcon(custom_icon_8cad53f2372f4d91b4d70834886e7d88);
        
    
            var marker_e2d4f45794fe4838a08a81b349c710cc = L.marker(
                [-17.2046852, 35.7804362],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_239c0fc2756e401aaae2ad8d60fc7e78 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_e2d4f45794fe4838a08a81b349c710cc.setIcon(custom_icon_239c0fc2756e401aaae2ad8d60fc7e78);
        
    
            var marker_5dd1790ab0314032bf4757d368f8441a = L.marker(
                [-15.7712666, 37.0844746],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_4bded1b3c14e41e9a731033c5080ba8c = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_5dd1790ab0314032bf4757d368f8441a.setIcon(custom_icon_4bded1b3c14e41e9a731033c5080ba8c);
        
    
            var marker_5fa45d20a02a4241bc8438777222ebf3 = L.marker(
                [-16.8003641, 36.5793288],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ac393b1dcfe0452587351750d4e66448 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_5fa45d20a02a4241bc8438777222ebf3.setIcon(custom_icon_ac393b1dcfe0452587351750d4e66448);
        
    
            var marker_122ae82bc8564e269b9467ba109864d6 = L.marker(
                [-16.2172005, 35.4791796],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_f01a11c882de4958a6ac9b3666a906f1 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_122ae82bc8564e269b9467ba109864d6.setIcon(custom_icon_f01a11c882de4958a6ac9b3666a906f1);
        
    
            var marker_691e2e45d7264b18a15ce7fa7a6561e2 = L.marker(
                [-17.6030474, 36.8195938],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_d2e29e11dd0340afbef4f09e0966ca5d = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_691e2e45d7264b18a15ce7fa7a6561e2.setIcon(custom_icon_d2e29e11dd0340afbef4f09e0966ca5d);
        
    
            var marker_364dcfebebdb49d1b2d02c5bfb40c226 = L.marker(
                [-16.4339325, 37.5887977],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_27a7a83870f74f84959cd92c4e26a795 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_364dcfebebdb49d1b2d02c5bfb40c226.setIcon(custom_icon_27a7a83870f74f84959cd92c4e26a795);
        
    
            var marker_480345c3834c4f438620257c98392bd9 = L.marker(
                [-15.7637306, 37.7554547],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_d41a5ebf6ecb400d961d13fe3e56e1fc = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_480345c3834c4f438620257c98392bd9.setIcon(custom_icon_d41a5ebf6ecb400d961d13fe3e56e1fc);
        
    
            var marker_520fcc0a327240c693ba88420c5acc62 = L.marker(
                [-16.7890677, 38.8739312],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_2689c56a28f64fef860ba9f414aaead5 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_520fcc0a327240c693ba88420c5acc62.setIcon(custom_icon_2689c56a28f64fef860ba9f414aaead5);
        
    
            var marker_9334643769cb4f7cb5ec55b8afe9f32e = L.marker(
                [-17.1417278, 35.3217718],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_bdf57c566fb34415b7bf06a06c4aee89 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_9334643769cb4f7cb5ec55b8afe9f32e.setIcon(custom_icon_bdf57c566fb34415b7bf06a06c4aee89);
        
    
            var marker_51e0d517b38348d8a3fe29240aab9c18 = L.marker(
                [-16.5171374, 37.1670216],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_048ee69b177e48a88789648c7641872c = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_51e0d517b38348d8a3fe29240aab9c18.setIcon(custom_icon_048ee69b177e48a88789648c7641872c);
        
    
            var marker_20f327bd629441e6a7fbfe387a6eb065 = L.marker(
                [-15.539836, 37.1931403],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_e442a20db8654dbe9968af174234494b = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_20f327bd629441e6a7fbfe387a6eb065.setIcon(custom_icon_e442a20db8654dbe9968af174234494b);
        
    
            var marker_a418b96771f743b0833dc1fe91735b26 = L.marker(
                [-18.4049737, 36.1079132],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_27db9e6df07f4a79af093c8c4dbe68f7 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_a418b96771f743b0833dc1fe91735b26.setIcon(custom_icon_27db9e6df07f4a79af093c8c4dbe68f7);
        
    
            var marker_1872ffd1dbc547b48f104c6ad394fdb0 = L.marker(
                [-16.7503883, 36.942858],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_c56598406090475f8f24a6587bb98ef7 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_1872ffd1dbc547b48f104c6ad394fdb0.setIcon(custom_icon_c56598406090475f8f24a6587bb98ef7);
        
    
            var marker_327f537bd0c34044a6790f09a70b1a85 = L.marker(
                [-15.9744715, 38.5498741],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_78f8a8c6eb0b4f30814c238128afaf9b = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_327f537bd0c34044a6790f09a70b1a85.setIcon(custom_icon_78f8a8c6eb0b4f30814c238128afaf9b);
        
    
            var marker_9276c98486fc4ee7918b13a683ddfaf6 = L.marker(
                [-17.1520484, 38.2791198],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_7d28bea917914f83b1202d4371cc2344 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_9276c98486fc4ee7918b13a683ddfaf6.setIcon(custom_icon_7d28bea917914f83b1202d4371cc2344);
        
    
            var marker_885eb63864f64c81bbf8babc8d18f3b9 = L.marker(
                [-16.5446964, 35.1780429],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_81208fde4a8a4421932428f257157233 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_885eb63864f64c81bbf8babc8d18f3b9.setIcon(custom_icon_81208fde4a8a4421932428f257157233);
        
    
            var marker_b728096dcb244d369aa748ec6bd054e5 = L.marker(
                [-17.7786413, 37.058533],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_5174afbc94904b00852186a623c5eef0 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_b728096dcb244d369aa748ec6bd054e5.setIcon(custom_icon_5174afbc94904b00852186a623c5eef0);
        
    
            var marker_7b18a5bc547b4cb483a20b02a77f0b04 = L.marker(
                [-17.9766704, 36.8579963],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_f71b71d5e0fa4560854240180f036258 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_7b18a5bc547b4cb483a20b02a77f0b04.setIcon(custom_icon_f71b71d5e0fa4560854240180f036258);
        
    
            var marker_1b5b602412224989b86f1c4a595130ce = L.marker(
                [-17.9798722, 35.7150386],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_66c4160522cc412cb83b470ce6f3154d = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_1b5b602412224989b86f1c4a595130ce.setIcon(custom_icon_66c4160522cc412cb83b470ce6f3154d);
        
    
            var marker_d1a2ffa9b1a84667801974d8ee55c80a = L.marker(
                [-16.7626269, 39.2231534],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_3f91f975fc8548b8a313bb28252c4d12 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_d1a2ffa9b1a84667801974d8ee55c80a.setIcon(custom_icon_3f91f975fc8548b8a313bb28252c4d12);
        
    
            var marker_e815afe22d394d6cb9118b73ad06d0f3 = L.marker(
                [-17.3271781, 35.5765361],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_5bb9f764134a486aa52d94fab2e76e76 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_e815afe22d394d6cb9118b73ad06d0f3.setIcon(custom_icon_5bb9f764134a486aa52d94fab2e76e76);
        
    
            var marker_b5ab9d2dc293412f9feb242550190f5c = L.marker(
                [-18.5695036, 36.1945076],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_cb4da656cbbf45a18362dfeda3c98c6a = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_b5ab9d2dc293412f9feb242550190f5c.setIcon(custom_icon_cb4da656cbbf45a18362dfeda3c98c6a);
        
    
            var marker_5613d9a8836c4937abbf48a9de1f4509 = L.marker(
                [-17.2636792, 37.8936817],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_86c7cf45bc1e44e3903576a353d1d7b7 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_5613d9a8836c4937abbf48a9de1f4509.setIcon(custom_icon_86c7cf45bc1e44e3903576a353d1d7b7);
        
    
            var marker_70c0ef8f0aa042dd8819d167d6b32be1 = L.marker(
                [-17.3280525, 35.5760384],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_d05d48ec701c46db997c09a418420e83 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_70c0ef8f0aa042dd8819d167d6b32be1.setIcon(custom_icon_d05d48ec701c46db997c09a418420e83);
        
    
            var marker_db0fdbb6e7314139aec9ec615ad339f5 = L.marker(
                [-15.7070731, 37.6417589],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_d5cd42c81b9e471aab358ccc8b1c6315 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_db0fdbb6e7314139aec9ec615ad339f5.setIcon(custom_icon_d5cd42c81b9e471aab358ccc8b1c6315);
        
    
            var marker_3c0ecdf2263e48f09659c5e0ea8eb681 = L.marker(
                [-13.9814648, 39.2315796],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_5c3785abbe1f46308580dff01ff3550d = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_3c0ecdf2263e48f09659c5e0ea8eb681.setIcon(custom_icon_5c3785abbe1f46308580dff01ff3550d);
        
    
            var marker_cd84578b7b724b6ebef938a5ffa41389 = L.marker(
                [-23.330834, 35.3812096],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a9ea6d5c7fef40f1bfbba02ab1f33411 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_cd84578b7b724b6ebef938a5ffa41389.setIcon(custom_icon_a9ea6d5c7fef40f1bfbba02ab1f33411);
        
    
            var marker_bcbaeb57632b45b4945bea76ca3cda41 = L.marker(
                [-17.1192523, 36.970472],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ed465f83829e46e1822ee46765834d30 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_bcbaeb57632b45b4945bea76ca3cda41.setIcon(custom_icon_ed465f83829e46e1822ee46765834d30);
        
    
            var marker_99fc08ab6f864f14b1ddc5230753f4c1 = L.marker(
                [-17.6159674, 35.523136],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_08aba01afefa4b0284c28b5ea80dcc28 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_99fc08ab6f864f14b1ddc5230753f4c1.setIcon(custom_icon_08aba01afefa4b0284c28b5ea80dcc28);
        
    
            var marker_229b8f913fd3435a80af61a79129f47b = L.marker(
                [-19.6300442, 34.7576335],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_b03fceda8f9b48058f3ee8b8906ce678 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_229b8f913fd3435a80af61a79129f47b.setIcon(custom_icon_b03fceda8f9b48058f3ee8b8906ce678);
        
    
            var marker_84990de84abb4050887c8819bd4c95e7 = L.marker(
                [-11.6630933, 39.5535949],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_aea55f07aae44969bf7ef6787959e5ef = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_84990de84abb4050887c8819bd4c95e7.setIcon(custom_icon_aea55f07aae44969bf7ef6787959e5ef);
        
    
            var marker_a4f144f5143247e1a215d0c9feb7c03a = L.marker(
                [-17.4944, 37.0265007],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_3ae3b8f60de848d19ace507724981b55 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_a4f144f5143247e1a215d0c9feb7c03a.setIcon(custom_icon_3ae3b8f60de848d19ace507724981b55);
        
    
            var marker_fe4e55ca43344ab78562892c5b0c719e = L.marker(
                [-15.4625448, 36.9826291],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_e95cb0a30fa64a5286e8019669349f47 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_fe4e55ca43344ab78562892c5b0c719e.setIcon(custom_icon_e95cb0a30fa64a5286e8019669349f47);
        
    
            var marker_2ae6328d091c4ea893f59750b17834bc = L.marker(
                [-16.3669335, 36.5152106],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_c2b7ec7f18c3476aacedbe34b01293ab = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_2ae6328d091c4ea893f59750b17834bc.setIcon(custom_icon_c2b7ec7f18c3476aacedbe34b01293ab);
        
    
            var marker_d00c6a29fbe74559968fe23c5a4d8c5d = L.marker(
                [-14.5586962, 40.7000159],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_d0807b7a8ddc4c08b68ce84ddd3e51a3 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_d00c6a29fbe74559968fe23c5a4d8c5d.setIcon(custom_icon_d0807b7a8ddc4c08b68ce84ddd3e51a3);
        
    
            var marker_e5c747a67d794f5a9fae96a139931a15 = L.marker(
                [-21.6643887, 35.4388724],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_00afc860565246d8983a98a6f8b35f8b = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_e5c747a67d794f5a9fae96a139931a15.setIcon(custom_icon_00afc860565246d8983a98a6f8b35f8b);
        
    
            var marker_22face0cce7b49a887f3aa6e40c9f4ec = L.marker(
                [-16.0934297, 37.3364829],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_b31fc9ac768947dfa233eaa94c685ce6 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_22face0cce7b49a887f3aa6e40c9f4ec.setIcon(custom_icon_b31fc9ac768947dfa233eaa94c685ce6);
        
    
            var marker_0db6e36ac6a245578ba0ed194ceb94e4 = L.marker(
                [-19.108944, 33.4778671],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_6d48630cddb2492481057e141435cc37 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_0db6e36ac6a245578ba0ed194ceb94e4.setIcon(custom_icon_6d48630cddb2492481057e141435cc37);
        
    
            var marker_6c13d87a531d4070a968bbef8078735d = L.marker(
                [-15.9903327, 37.3570072],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_431ec8e2a8d444ddb35ae0b534dc003f = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_6c13d87a531d4070a968bbef8078735d.setIcon(custom_icon_431ec8e2a8d444ddb35ae0b534dc003f);
        
    
            var marker_20a478006a5d4532a5149c4d608d1a14 = L.marker(
                [-18.0100914, 36.8107183],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ced3d074acdc406f8305ff2b88e8312f = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_20a478006a5d4532a5149c4d608d1a14.setIcon(custom_icon_ced3d074acdc406f8305ff2b88e8312f);
        
    
            var marker_7bb5db9f927140fe85175276ca741b18 = L.marker(
                [-15.749312, 36.7891145],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_011572c1502a4190b9e75809f96e650e = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_7bb5db9f927140fe85175276ca741b18.setIcon(custom_icon_011572c1502a4190b9e75809f96e650e);
        
    
            var marker_789574232fd24a2eaa0c366c786f8b17 = L.marker(
                [-17.1034196, 37.97842],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ac4fa583465c4fe3950d3b7b26e43c74 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_789574232fd24a2eaa0c366c786f8b17.setIcon(custom_icon_ac4fa583465c4fe3950d3b7b26e43c74);
        
    
            var marker_66cee3121dce4dd1b0651db8642e1ad9 = L.marker(
                [-17.207052, 36.2794653],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_df04619ff3b94eba9f747bc224112c4e = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_66cee3121dce4dd1b0651db8642e1ad9.setIcon(custom_icon_df04619ff3b94eba9f747bc224112c4e);
        
    
            var marker_d4b25bd8b7164eeb93e3b7b95dfeae22 = L.marker(
                [-14.5101051, 40.6803372],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_95c42e135952454aaafa50056f353cb6 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_d4b25bd8b7164eeb93e3b7b95dfeae22.setIcon(custom_icon_95c42e135952454aaafa50056f353cb6);
        
    
            var marker_16598b29b5a243c3bc91d708ad86aaae = L.marker(
                [-14.9159844, 40.2989151],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_627fd331dab54ec2927d8284bb57e022 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_16598b29b5a243c3bc91d708ad86aaae.setIcon(custom_icon_627fd331dab54ec2927d8284bb57e022);
        
    
            var marker_8368cc94230f43bd9dd187f6fb72bc5c = L.marker(
                [-17.5753002, 37.1589012],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_629f5da2f6834488945bf33b7e99626b = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_8368cc94230f43bd9dd187f6fb72bc5c.setIcon(custom_icon_629f5da2f6834488945bf33b7e99626b);
        
    
            var marker_77a49d6724ce4d7b82a10ad7af3615f5 = L.marker(
                [-15.4883014, 37.1401707],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_8c1d809be3ed4ba09cab5422725bd38b = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_77a49d6724ce4d7b82a10ad7af3615f5.setIcon(custom_icon_8c1d809be3ed4ba09cab5422725bd38b);
        
    
            var marker_7397bac1cac3427db94b3764d5560cba = L.marker(
                [-12.45862, 37.6616183],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_47a8f6bd75d04c83949709688473f2d0 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_7397bac1cac3427db94b3764d5560cba.setIcon(custom_icon_47a8f6bd75d04c83949709688473f2d0);
        
    
            var marker_d04dbce4f62a4d73bd0d045eb9c5ac38 = L.marker(
                [-19.077134, 33.6417192],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_dab93d340f714a81beb7e9d4ddcb346e = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_d04dbce4f62a4d73bd0d045eb9c5ac38.setIcon(custom_icon_dab93d340f714a81beb7e9d4ddcb346e);
        
    
            var marker_6433a6d0bfea4509bc6a37e7006b58eb = L.marker(
                [-17.0124868, 38.7192609],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_efae1230a32241079d2b2f134af8b275 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_6433a6d0bfea4509bc6a37e7006b58eb.setIcon(custom_icon_efae1230a32241079d2b2f134af8b275);
        
    
            var marker_14241c5a51f14579bafbb2ff870484db = L.marker(
                [-16.0377927, 37.1681146],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_14c7b02055e0440e9763ff551405c4c1 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_14241c5a51f14579bafbb2ff870484db.setIcon(custom_icon_14c7b02055e0440e9763ff551405c4c1);
        
    
            var marker_0970e56c20c94991b69a10f2a2e86206 = L.marker(
                [-15.5678606, 37.3589753],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_3075dfca0037458f99c7e4f19151733b = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_0970e56c20c94991b69a10f2a2e86206.setIcon(custom_icon_3075dfca0037458f99c7e4f19151733b);
        
    
            var marker_a0d34d4ffada4e9695a78ba8dce0b830 = L.marker(
                [-15.7843092, 37.1633115],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_37e6231b9c774ea99e935130b81400cf = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_a0d34d4ffada4e9695a78ba8dce0b830.setIcon(custom_icon_37e6231b9c774ea99e935130b81400cf);
        
    
            var marker_5ffa2a5ddebb4d6eae05c54927531936 = L.marker(
                [-16.2692763, 37.5162855],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_4171371e43e84cdeb44e864aa8a80b85 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_5ffa2a5ddebb4d6eae05c54927531936.setIcon(custom_icon_4171371e43e84cdeb44e864aa8a80b85);
        
    
            var marker_c843b3e7247a474fb4e172e7c6a6bad7 = L.marker(
                [-15.3863976, 36.5264417],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_8ac6bea420ec4376b3d84582ffcc6ae1 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_c843b3e7247a474fb4e172e7c6a6bad7.setIcon(custom_icon_8ac6bea420ec4376b3d84582ffcc6ae1);
        
    
            var marker_80a3b513003f400d9b047a7c4ac5ca88 = L.marker(
                [-15.0342222, 40.7351646],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_18f856c1d0b9439994eb2e40e524da6f = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_80a3b513003f400d9b047a7c4ac5ca88.setIcon(custom_icon_18f856c1d0b9439994eb2e40e524da6f);
        
    
            var marker_bdd18de84adb4741ad682961eae18a89 = L.marker(
                [-17.7107572, 37.2501413],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_6b75ac8773e44e299f1d7cd2b2e787ee = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_bdd18de84adb4741ad682961eae18a89.setIcon(custom_icon_6b75ac8773e44e299f1d7cd2b2e787ee);
        
    
            var marker_e2f95750ddab4ab3b6f22825bb9496a1 = L.marker(
                [-15.644225, 37.679522],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_9a2dbf7573ba452199d9fa9c16be6a1a = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_e2f95750ddab4ab3b6f22825bb9496a1.setIcon(custom_icon_9a2dbf7573ba452199d9fa9c16be6a1a);
        
    
            var marker_fa67d95cba1e4bf5b6dcbcf5f5d8916a = L.marker(
                [-14.5518561, 40.6722611],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_90684c8927cd42b7bf5116f06d4256ea = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_fa67d95cba1e4bf5b6dcbcf5f5d8916a.setIcon(custom_icon_90684c8927cd42b7bf5116f06d4256ea);
        
    
            var marker_6d0c3e8bf69e4a9db0d8020a59222701 = L.marker(
                [-17.3092282, 37.5088879],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_5a5e63c40fb448149324a4e699eb03fd = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_6d0c3e8bf69e4a9db0d8020a59222701.setIcon(custom_icon_5a5e63c40fb448149324a4e699eb03fd);
        
    
            var marker_447ef23acf094e4fa644b5f442c7575c = L.marker(
                [-17.009507, 37.4875074],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_311f30c4d99845899d07225e662439c0 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_447ef23acf094e4fa644b5f442c7575c.setIcon(custom_icon_311f30c4d99845899d07225e662439c0);
        
    
            var marker_d6a209ccdfc143d29cbe4c4f6a188f50 = L.marker(
                [-17.7389414, 36.5363156],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_1aff3b13c2de43e49739ea223960f404 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_d6a209ccdfc143d29cbe4c4f6a188f50.setIcon(custom_icon_1aff3b13c2de43e49739ea223960f404);
        
    
            var marker_81c7d9b214c745658d8b655f80dd87b1 = L.marker(
                [-24.5354251, 33.0054376],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_38d6fa66b7f64290b90f4433e1c5a29d = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_81c7d9b214c745658d8b655f80dd87b1.setIcon(custom_icon_38d6fa66b7f64290b90f4433e1c5a29d);
        
    
            var marker_47f7b023276e4e03a24bd703f41aa126 = L.marker(
                [-16.7667284, 37.5958908],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_2d46e8aaa9d741e3ba66334045134e88 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_47f7b023276e4e03a24bd703f41aa126.setIcon(custom_icon_2d46e8aaa9d741e3ba66334045134e88);
        
    
            var marker_1bb1969532484261b6f40341d250a6a5 = L.marker(
                [-14.4924498, 40.7065974],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_cfb2776884f44cb0b22e0c3723948092 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_1bb1969532484261b6f40341d250a6a5.setIcon(custom_icon_cfb2776884f44cb0b22e0c3723948092);
        
    
            var marker_dbcf9b1d5b4542849045b62b25451f60 = L.marker(
                [-20.4529642, 32.7721578],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a50cf5e38c5f477faa9de9e49e2dfbb8 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_dbcf9b1d5b4542849045b62b25451f60.setIcon(custom_icon_a50cf5e38c5f477faa9de9e49e2dfbb8);
        
    
            var marker_034c23fa2b5f4ca08082eca62fa43f48 = L.marker(
                [-16.4680635, 35.8156603],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_c4f989fc44e5446ca972f65b35bd470d = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_034c23fa2b5f4ca08082eca62fa43f48.setIcon(custom_icon_c4f989fc44e5446ca972f65b35bd470d);
        
    
            var marker_2a92a98943f64687aa287d188456988c = L.marker(
                [-17.8190442, 36.9467378],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_b11dc7de8a4545d684a3380716c8e292 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_2a92a98943f64687aa287d188456988c.setIcon(custom_icon_b11dc7de8a4545d684a3380716c8e292);
        
    
            var marker_7b60d308a83042078e5c0219ba897f28 = L.marker(
                [-17.8456062, 35.4770174],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_d76625e9e3a94baea926607b9d4e23cf = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_7b60d308a83042078e5c0219ba897f28.setIcon(custom_icon_d76625e9e3a94baea926607b9d4e23cf);
        
    
            var marker_cbca0d5e1bb94b95864da64be1fb4943 = L.marker(
                [-14.9464889, 38.3208098],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_5f9f79c5cbd749b5bbd07cc228dc775b = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_cbca0d5e1bb94b95864da64be1fb4943.setIcon(custom_icon_5f9f79c5cbd749b5bbd07cc228dc775b);
        
    
            var marker_f7d0b97920484c56b61e424d3bbce095 = L.marker(
                [-19.6161877, 34.7411342],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_f69bcab379c747ccbcfc7d26b8f74695 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_f7d0b97920484c56b61e424d3bbce095.setIcon(custom_icon_f69bcab379c747ccbcfc7d26b8f74695);
        
    
            var marker_0abf7760295f45af9e8d2172f8a2aca6 = L.marker(
                [-15.0862388, 39.2876664],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_8e9581a178b948529494a21e0a8b75a5 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_0abf7760295f45af9e8d2172f8a2aca6.setIcon(custom_icon_8e9581a178b948529494a21e0a8b75a5);
        
    
            var marker_72ee7493cd7c4e37b2a02356b0676b54 = L.marker(
                [-25.9092672, 32.5673125],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_70856914de9441abbaf3df65572136aa = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_72ee7493cd7c4e37b2a02356b0676b54.setIcon(custom_icon_70856914de9441abbaf3df65572136aa);
        
    
            var marker_8b39adc087f447d3bd1775cb504da781 = L.marker(
                [-14.1268741, 40.1428209],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_d68b53e7d01f42219c4795d8eec5c9a0 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_8b39adc087f447d3bd1775cb504da781.setIcon(custom_icon_d68b53e7d01f42219c4795d8eec5c9a0);
        
    
            var marker_cf7e40b08d8549789dee4039390280f5 = L.marker(
                [-21.71758, 35.0943316],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_25b3fbb564574a71a748e70a0538e322 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_cf7e40b08d8549789dee4039390280f5.setIcon(custom_icon_25b3fbb564574a71a748e70a0538e322);
        
    
            var marker_e40756dc9a094cd48b81abf539aca833 = L.marker(
                [-21.7175252, 35.0946776],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_1c02a91b3a2d4267b6236164275704fc = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_e40756dc9a094cd48b81abf539aca833.setIcon(custom_icon_1c02a91b3a2d4267b6236164275704fc);
        
    
            var marker_dcc6be46019a4c7c8641c3aeb4b0c71c = L.marker(
                [-25.8566602, 32.6284423],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_76e8e193bbb9406286033acbcc72b54e = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_dcc6be46019a4c7c8641c3aeb4b0c71c.setIcon(custom_icon_76e8e193bbb9406286033acbcc72b54e);
        
    
            var marker_1d092f22782b4306b50170c8b059da56 = L.marker(
                [-12.9632009, 40.4933739],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_e773a645204548d1b39f59a9aa463e5c = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_1d092f22782b4306b50170c8b059da56.setIcon(custom_icon_e773a645204548d1b39f59a9aa463e5c);
        
    
            var marker_9ed90dc4d37043209228de7e62dd59f3 = L.marker(
                [-13.0599521, 40.5251017],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a3ec2a92de1e4d71bbfdaa7c773fa3c7 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_9ed90dc4d37043209228de7e62dd59f3.setIcon(custom_icon_a3ec2a92de1e4d71bbfdaa7c773fa3c7);
        
    
            var marker_308100c7d0244769829483d6a0c1f748 = L.marker(
                [-13.0224015, 40.5655655],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_9ee084885aa045eeba8a38f2959b52b3 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_308100c7d0244769829483d6a0c1f748.setIcon(custom_icon_9ee084885aa045eeba8a38f2959b52b3);
        
    
            var marker_9ba4e3c5150c4f5cb87277673c199373 = L.marker(
                [-13.0192525, 40.5292484],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_b58a2cc2fe6d41d499c1c34596f80d04 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_9ba4e3c5150c4f5cb87277673c199373.setIcon(custom_icon_b58a2cc2fe6d41d499c1c34596f80d04);
        
    
            var marker_4cb87792bbbf46bb81f8156c1b4feaaf = L.marker(
                [-23.287093, 35.4294945],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_f66f6d7417e745f890800f7e0a7968fe = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_4cb87792bbbf46bb81f8156c1b4feaaf.setIcon(custom_icon_f66f6d7417e745f890800f7e0a7968fe);
        
    
            var marker_ef6474e3aded40429ca8b3dd3c772e69 = L.marker(
                [-22.8738373, 35.3016949],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_f8712324ffdc4df29f92498aeaec7809 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_ef6474e3aded40429ca8b3dd3c772e69.setIcon(custom_icon_f8712324ffdc4df29f92498aeaec7809);
        
    
            var marker_b7030ebfb2fa412aa90507c2307ceac8 = L.marker(
                [-23.1948063, 35.3820335],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_b324abffd0e949a1af64afc8b3643d59 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_b7030ebfb2fa412aa90507c2307ceac8.setIcon(custom_icon_b324abffd0e949a1af64afc8b3643d59);
        
    
            var marker_84e4902c2d264574842c57434c2d2a9b = L.marker(
                [-23.3089642, 35.2799709],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_e168a7e4b41e49d0b47750dec8e26bc4 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_84e4902c2d264574842c57434c2d2a9b.setIcon(custom_icon_e168a7e4b41e49d0b47750dec8e26bc4);
        
    
            var marker_6c82ed19e5664b919a1f5986529203e5 = L.marker(
                [-22.7665337, 35.0202869],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_418f6fdd579640babbb2961a11e047d0 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_6c82ed19e5664b919a1f5986529203e5.setIcon(custom_icon_418f6fdd579640babbb2961a11e047d0);
        
    
            var marker_52ea61ad032047448a336fe8677804f8 = L.marker(
                [-23.0904307, 35.1240155],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_23db0d98027a442ca44c821ce64b9c28 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_52ea61ad032047448a336fe8677804f8.setIcon(custom_icon_23db0d98027a442ca44c821ce64b9c28);
        
    
            var marker_841e3bda5dc84ba791c8d4dfcb21ad58 = L.marker(
                [-22.9627257, 35.4462515],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_280a237d58f34b24b8c89aef2da0b9f3 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_841e3bda5dc84ba791c8d4dfcb21ad58.setIcon(custom_icon_280a237d58f34b24b8c89aef2da0b9f3);
        
    
            var marker_09403311913d41f6a8d50a4a999f235d = L.marker(
                [-23.429598, 35.3374827],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_6f13c2680d7a426a84c9aa58a2cd3eef = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_09403311913d41f6a8d50a4a999f235d.setIcon(custom_icon_6f13c2680d7a426a84c9aa58a2cd3eef);
        
    
            var marker_427b465fed034901ad63fbb79408a03b = L.marker(
                [-23.0915088, 34.3806123],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_6c22ae2ed38a4125a53a1caf3272b55d = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_427b465fed034901ad63fbb79408a03b.setIcon(custom_icon_6c22ae2ed38a4125a53a1caf3272b55d);
        
    
            var marker_6ba2212eed0b4fb08e5cffcb4467dc74 = L.marker(
                [-23.1257925, 34.6398009],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_aa4f32cf5d1d4937a9a30297842c8551 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_6ba2212eed0b4fb08e5cffcb4467dc74.setIcon(custom_icon_aa4f32cf5d1d4937a9a30297842c8551);
        
    
            var marker_16ea208e6c2d49c0b089782c89387acc = L.marker(
                [-23.4254576, 34.4978954],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_69cdd28fc7d442dea9c1cc016451c6eb = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_16ea208e6c2d49c0b089782c89387acc.setIcon(custom_icon_69cdd28fc7d442dea9c1cc016451c6eb);
        
    
            var marker_27e7e711acc1423b92a6ac3ff40b84a9 = L.marker(
                [-22.5404533, 34.1916482],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_49ece3354ed44d99995bb1462f827a37 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_27e7e711acc1423b92a6ac3ff40b84a9.setIcon(custom_icon_49ece3354ed44d99995bb1462f827a37);
        
    
            var marker_041387af9eaa45258d8b602658367bc6 = L.marker(
                [-22.8120061, 34.0150534],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_0c18504c0a424c4993acd1ddc084b1d3 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_041387af9eaa45258d8b602658367bc6.setIcon(custom_icon_0c18504c0a424c4993acd1ddc084b1d3);
        
    
            var marker_a608a0aac304493cb3b173480e9075ef = L.marker(
                [-25.9072345, 32.6159809],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_7041de0ae38a4a3caf1d260192a1f395 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_a608a0aac304493cb3b173480e9075ef.setIcon(custom_icon_7041de0ae38a4a3caf1d260192a1f395);
        
    
            var marker_298083d6a2e540f3b6b9085277e7b615 = L.marker(
                [-25.9019082, 32.6171013],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_e251677b5b004601bdb2e55cfc438d0e = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_298083d6a2e540f3b6b9085277e7b615.setIcon(custom_icon_e251677b5b004601bdb2e55cfc438d0e);
        
    
            var marker_98def8aeed914b8486749c757c64d0f0 = L.marker(
                [-25.8379251, 32.637147],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_21a9bf05d16c47239686c5bba516c9cd = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_98def8aeed914b8486749c757c64d0f0.setIcon(custom_icon_21a9bf05d16c47239686c5bba516c9cd);
        
    
            var marker_93ac6d75d8e04b549c180f8f2873bb37 = L.marker(
                [-25.8450558, 32.6335245],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_98c95b9161154cb4a32315d65a36abb8 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_93ac6d75d8e04b549c180f8f2873bb37.setIcon(custom_icon_98c95b9161154cb4a32315d65a36abb8);
        
    
            var marker_fe69fa6b9c864237a1d7d78cb397df07 = L.marker(
                [-16.8405386, 36.9870116],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_4ba9f40a150a49348157f4c57ffcf35a = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_fe69fa6b9c864237a1d7d78cb397df07.setIcon(custom_icon_4ba9f40a150a49348157f4c57ffcf35a);
        
    
            var marker_697426e10ae944649f982c799478b400 = L.marker(
                [-17.8664841, 36.8916098],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_efafa1c4f7e4448dacb7a8db701013f2 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_697426e10ae944649f982c799478b400.setIcon(custom_icon_efafa1c4f7e4448dacb7a8db701013f2);
        
    
            var marker_df4bdb5032a3407894e9ce2c3fe785cd = L.marker(
                [-25.9155492, 32.5190716],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_b2b4dcf039d743b68475fa895919cf6f = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_df4bdb5032a3407894e9ce2c3fe785cd.setIcon(custom_icon_b2b4dcf039d743b68475fa895919cf6f);
        
    
            var marker_b7ff73dc711c4bab80ae4f942a8b3511 = L.marker(
                [-25.9159189, 32.5197736],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_831bc09471cb47578926fdf1c789e044 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_b7ff73dc711c4bab80ae4f942a8b3511.setIcon(custom_icon_831bc09471cb47578926fdf1c789e044);
        
    
            var marker_d1c40566320b445cbd118d7916bc89a7 = L.marker(
                [-25.930397180019742, 32.58613324179911],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_49bb1036a4c14c489527ecd1d29a2ebc = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_d1c40566320b445cbd118d7916bc89a7.setIcon(custom_icon_49bb1036a4c14c489527ecd1d29a2ebc);
        
    
            var marker_b000ec855d4e448b93d3cd4bbc9ed5a4 = L.marker(
                [-25.96892094855812, 32.58887828621594],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_393a2b3bf65e4c83b541599522fec15a = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_b000ec855d4e448b93d3cd4bbc9ed5a4.setIcon(custom_icon_393a2b3bf65e4c83b541599522fec15a);
        
    
            var marker_ba3f4f99153a42c99ca0365c9fd4e879 = L.marker(
                [-21.993589277689072, 35.32004142030749],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_556992dcbd714b828a53c16b5eb0be71 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_ba3f4f99153a42c99ca0365c9fd4e879.setIcon(custom_icon_556992dcbd714b828a53c16b5eb0be71);
        
    
            var marker_e94547eaaf9443778698b70f5ea50f07 = L.marker(
                [-22.05080436833823, 35.320621160000364],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_64996ffbfc8c44c4b2d876cc9932ddc9 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_e94547eaaf9443778698b70f5ea50f07.setIcon(custom_icon_64996ffbfc8c44c4b2d876cc9932ddc9);
        
    
            var marker_8d5714c818ac4b11ad9e3f58bf459b88 = L.marker(
                [-24.53554589603149, 33.00551528893833],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_384e60f75a4341a2801d8bb176a6589a = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_8d5714c818ac4b11ad9e3f58bf459b88.setIcon(custom_icon_384e60f75a4341a2801d8bb176a6589a);
        
    
            var marker_62d0447e85be4a4185bba5de762a40d0 = L.marker(
                [-24.528498952624403, 33.00387785249616],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_96dcae1a16cf41b59860ae58c8a0d2e7 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_62d0447e85be4a4185bba5de762a40d0.setIcon(custom_icon_96dcae1a16cf41b59860ae58c8a0d2e7);
        
    
            var marker_31cf36268b374a78b85f49e7b6fc3cb9 = L.marker(
                [-24.495714786998555, 35.169708666998005],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_8c484b6c1d044991976bd4f09a0fff91 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_31cf36268b374a78b85f49e7b6fc3cb9.setIcon(custom_icon_8c484b6c1d044991976bd4f09a0fff91);
        
    
            var marker_d2f0d66a4c734634b32172abef3e2359 = L.marker(
                [-26.00325184801278, 32.92032175666005],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_9565d150aaa04cdd8ca05132e183f6eb = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_d2f0d66a4c734634b32172abef3e2359.setIcon(custom_icon_9565d150aaa04cdd8ca05132e183f6eb);
        
    
            var marker_f78bb5ed1f204e65a121f1186b7fe27e = L.marker(
                [-25.9741852, 32.583170550000006],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_3ab38fbbf5ab486da36cea9deb6247f2 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_f78bb5ed1f204e65a121f1186b7fe27e.setIcon(custom_icon_3ab38fbbf5ab486da36cea9deb6247f2);
        
    
            var marker_827f690627ff4aa3b02e86495e718aec = L.marker(
                [-25.947669162445617, 32.544021618604546],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_0591d1e8e32f41f3a92fd7b1e792b1c9 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_827f690627ff4aa3b02e86495e718aec.setIcon(custom_icon_0591d1e8e32f41f3a92fd7b1e792b1c9);
        
    
            var marker_c1fcbdae309e4abeb40e61fb3d4e4f6a = L.marker(
                [-25.96297205051207, 32.594457933640115],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a671d1f0e6944a8b88a6c183282ab501 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_c1fcbdae309e4abeb40e61fb3d4e4f6a.setIcon(custom_icon_a671d1f0e6944a8b88a6c183282ab501);
        
    
            var marker_7ec2905182d5415c93e8d7c68642d7a5 = L.marker(
                [-25.9347461510755, 32.60469798777849],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_325188648d5647aa8cf9a65314750fc8 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_7ec2905182d5415c93e8d7c68642d7a5.setIcon(custom_icon_325188648d5647aa8cf9a65314750fc8);
        
    
            var marker_bcb9eae95a7a410f90fcffe1319baf2c = L.marker(
                [-23.88100813263387, 35.152992958511064],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_3afec9f551df4bbd962e4acbea65b4da = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_bcb9eae95a7a410f90fcffe1319baf2c.setIcon(custom_icon_3afec9f551df4bbd962e4acbea65b4da);
        
    
            var marker_8079d72198164d3aaf3949f36085fa05 = L.marker(
                [-25.957259036931205, 32.59210926274451],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_79f20e5ac2de447e9cf6c045bd46fc16 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_8079d72198164d3aaf3949f36085fa05.setIcon(custom_icon_79f20e5ac2de447e9cf6c045bd46fc16);
        
    
            var marker_d2fe22a33750491686199fda22c16303 = L.marker(
                [-20.075365584204313, 32.91299724862023],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_8233fee8000642a8809bd253a9d57f4c = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_d2fe22a33750491686199fda22c16303.setIcon(custom_icon_8233fee8000642a8809bd253a9d57f4c);
        
    
            var marker_fe3c1e2b8649492d90f14a35a44b430e = L.marker(
                [-19.10904814096506, 33.47828742088708],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_c05f3695238f44c088d914eb038e11d9 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_fe3c1e2b8649492d90f14a35a44b430e.setIcon(custom_icon_c05f3695238f44c088d914eb038e11d9);
        
    
            var marker_341c3b80a7a649b29516ac1957c526cc = L.marker(
                [-15.03746844572203, 40.7315413848555],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_81cbc5b1757241e2a09cb9e7f605a9c3 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_341c3b80a7a649b29516ac1957c526cc.setIcon(custom_icon_81cbc5b1757241e2a09cb9e7f605a9c3);
        
    
            var marker_70450ac19b5e42c89ffafc90c0cd6c07 = L.marker(
                [-14.536883253754787, 40.63013073539269],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_6d29ad80081a40f3a93461c3e5672e41 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_70450ac19b5e42c89ffafc90c0cd6c07.setIcon(custom_icon_6d29ad80081a40f3a93461c3e5672e41);
        
    
            var marker_93b5bfed88c049d2abf185d821190bfa = L.marker(
                [-15.123271992561175, 39.26123783675845],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_8dbd2488effc4e0c910082e53df31e64 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_93b5bfed88c049d2abf185d821190bfa.setIcon(custom_icon_8dbd2488effc4e0c910082e53df31e64);
        
    
            var marker_36f6245816e8469697c1f6937467b59e = L.marker(
                [-18.10057159638579, 32.95543951429496],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_6fbc3f487d4a4f7d98c9a9e3fdac7a02 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_36f6245816e8469697c1f6937467b59e.setIcon(custom_icon_6fbc3f487d4a4f7d98c9a9e3fdac7a02);
        
    
            var marker_61920af8995b457b83205616b8b3ddec = L.marker(
                [-15.112779708440984, 39.223317767130325],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_13e6993249224b44b5353233887245c1 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_61920af8995b457b83205616b8b3ddec.setIcon(custom_icon_13e6993249224b44b5353233887245c1);
        
    
            var marker_68ceb8d7be8c4d2ba37ae34d4ee2d221 = L.marker(
                [-15.131328240680228, 39.25170910923652],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_29d4dcc4fdd94e7093201644d8d312a3 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_68ceb8d7be8c4d2ba37ae34d4ee2d221.setIcon(custom_icon_29d4dcc4fdd94e7093201644d8d312a3);
        
    
            var marker_157c5d0557ed40c8a81bbe8079d6c4be = L.marker(
                [-15.253897802195832, 39.24829486859653],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_31a5f5f99b6a43b69a68c8d78d9e63ea = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_157c5d0557ed40c8a81bbe8079d6c4be.setIcon(custom_icon_31a5f5f99b6a43b69a68c8d78d9e63ea);
        
    
            var marker_d22b9eb8cf194efeb87d4680db2b8f21 = L.marker(
                [-15.254064199999998, 39.248625399999995],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_56bafd1d889d45498b97a56bd8b65c07 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_d22b9eb8cf194efeb87d4680db2b8f21.setIcon(custom_icon_56bafd1d889d45498b97a56bd8b65c07);
        
    
            var marker_0776cc49fb8d40d884829f5e76bd4942 = L.marker(
                [-15.253861316784992, 39.24850969985975],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_faadb2ee9fd1414aad02053b4b1fe1f0 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_0776cc49fb8d40d884829f5e76bd4942.setIcon(custom_icon_faadb2ee9fd1414aad02053b4b1fe1f0);
        
    
            var marker_61cd7af5422e4a4d85931ce2dad61555 = L.marker(
                [-15.254029103541118, 39.24842181854006],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_0b84378c010b4c8e81bd1328f163ef4f = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_61cd7af5422e4a4d85931ce2dad61555.setIcon(custom_icon_0b84378c010b4c8e81bd1328f163ef4f);
        
    
            var marker_6df84365c1fd48519000b05433decf64 = L.marker(
                [-15.253835436861577, 39.24831302447477],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_67db8da787124097b1bb3fad81082bf8 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_6df84365c1fd48519000b05433decf64.setIcon(custom_icon_67db8da787124097b1bb3fad81082bf8);
        
    
            var marker_953670b8eba748a7be9f186689bdab5e = L.marker(
                [-15.25376958496918, 39.2486175708511],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_98f67fa070c846e4bd285e60a1d719fd = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_953670b8eba748a7be9f186689bdab5e.setIcon(custom_icon_98f67fa070c846e4bd285e60a1d719fd);
        
    
            var marker_ea12a7d4617440e49d81d42c4e8dfcb5 = L.marker(
                [-15.253818484701084, 39.248113752254056],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_22e7cea19c7240f894e715a7ad760d85 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_ea12a7d4617440e49d81d42c4e8dfcb5.setIcon(custom_icon_22e7cea19c7240f894e715a7ad760d85);
        
    
            var marker_51867dd5832447d58e7a6a7090d2ecf6 = L.marker(
                [-15.253967617851501, 39.24844743838863],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_bbe9c4307cc84c7a82aedc6463adb733 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_51867dd5832447d58e7a6a7090d2ecf6.setIcon(custom_icon_bbe9c4307cc84c7a82aedc6463adb733);
        
    
            var marker_d4b4593fc7264ac5ab8a8afb92b42cbf = L.marker(
                [-15.25389985, 39.248174549999995],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_dd0f2122bfd84c888e34ada9427f0957 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_d4b4593fc7264ac5ab8a8afb92b42cbf.setIcon(custom_icon_dd0f2122bfd84c888e34ada9427f0957);
        
    
            var marker_95b3e20771934816855eebe1f209d1cf = L.marker(
                [-16.0980249882152, 35.78125579677181],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_b0fb3427d2ef4902af3e39ac0a8b9346 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_95b3e20771934816855eebe1f209d1cf.setIcon(custom_icon_b0fb3427d2ef4902af3e39ac0a8b9346);
        
    
            var marker_34c262f236884423b9042b877a5d7fd8 = L.marker(
                [-23.88642212012623, 35.47108413192305],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_0ccf5c74bcd74c16980c4593f51aa509 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_34c262f236884423b9042b877a5d7fd8.setIcon(custom_icon_0ccf5c74bcd74c16980c4593f51aa509);
        
    
            var marker_bad17fb07d214b3095c66c23842bb90b = L.marker(
                [-16.098989222643063, 35.76901702619338],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_6f793067e5504951a1213c2481741316 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_bad17fb07d214b3095c66c23842bb90b.setIcon(custom_icon_6f793067e5504951a1213c2481741316);
        
    
            var marker_7ac32500eb5547f190917a89aee6789c = L.marker(
                [-25.96727836195467, 32.438579365511565],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_72e37b4144e14fe19d63e5ccb235909c = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_7ac32500eb5547f190917a89aee6789c.setIcon(custom_icon_72e37b4144e14fe19d63e5ccb235909c);
        
    
            var marker_1b18b97afa264292aba328a596616b6f = L.marker(
                [-25.942995401521074, 32.61132882431118],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ed62e0555755485e81200cf2c4dc8043 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_1b18b97afa264292aba328a596616b6f.setIcon(custom_icon_ed62e0555755485e81200cf2c4dc8043);
        
    
            var marker_8f397637e96d4550a277c112891610d4 = L.marker(
                [-25.914996382345123, 32.609902329315986],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_178908bc4c9542eebda8f9909ecb54dc = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_8f397637e96d4550a277c112891610d4.setIcon(custom_icon_178908bc4c9542eebda8f9909ecb54dc);
        
    
            var marker_40576da3ec83430eabdd77394cbb3fb5 = L.marker(
                [-25.40877778233415, 32.80720743939425],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_2e663260b2a0468098d95d5e71868111 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_40576da3ec83430eabdd77394cbb3fb5.setIcon(custom_icon_2e663260b2a0468098d95d5e71868111);
        
    
            var marker_ae33def2802b487abcb1c37c881da1e0 = L.marker(
                [-22.921402481753486, 35.53661387183501],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_d0b3c1f410574ebea88c716f1f074f55 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_ae33def2802b487abcb1c37c881da1e0.setIcon(custom_icon_d0b3c1f410574ebea88c716f1f074f55);
        
    
            var marker_a96d9534fd164807b7e5e9e9b13f4b69 = L.marker(
                [-17.97916682570036, 35.71261206400323],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_3d4981f8d3a14299a48665d12eccf33a = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_a96d9534fd164807b7e5e9e9b13f4b69.setIcon(custom_icon_3d4981f8d3a14299a48665d12eccf33a);
        
    
            var marker_e4e0fb0abe5b45208d9848a52dd3df78 = L.marker(
                [-17.32736254120817, 35.57655724237055],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_0a3956289dfe4e419bf97d9bfc9c6732 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_e4e0fb0abe5b45208d9848a52dd3df78.setIcon(custom_icon_0a3956289dfe4e419bf97d9bfc9c6732);
        
    
            var marker_e02394cb66e44fae805cc9f0f11e2b82 = L.marker(
                [-17.493929303471436, 37.03295577896049],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_f1bd783ef5ec4b158de42236f0b466e3 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_e02394cb66e44fae805cc9f0f11e2b82.setIcon(custom_icon_f1bd783ef5ec4b158de42236f0b466e3);
        
    
            var marker_2aceb19dc6b94fe7bb2eac1120f87b4b = L.marker(
                [-16.153139263303, 33.579654816565004],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_6f86841313874478be7fcc606efd2da0 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_2aceb19dc6b94fe7bb2eac1120f87b4b.setIcon(custom_icon_6f86841313874478be7fcc606efd2da0);
        
    
            var marker_98d2b1703f6345a489dd27ba32a99130 = L.marker(
                [-17.493322004854324, 37.02659352894958],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_bf2e943d9dfc41259ffffcc16ca9b6fc = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_98d2b1703f6345a489dd27ba32a99130.setIcon(custom_icon_bf2e943d9dfc41259ffffcc16ca9b6fc);
        
    
            var marker_c4f416d296c04db796e378e34884e5b6 = L.marker(
                [-19.11097365473498, 33.47642396986647],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_88e4679c08324e9cb37cea0b65ba606a = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_c4f416d296c04db796e378e34884e5b6.setIcon(custom_icon_88e4679c08324e9cb37cea0b65ba606a);
        
    
            var marker_c6728280521744c4a10dfc33da990ec7 = L.marker(
                [-19.108919147660938, 33.47082521422588],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_3d588040cbb442a2a061ed094d1c2500 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_c6728280521744c4a10dfc33da990ec7.setIcon(custom_icon_3d588040cbb442a2a061ed094d1c2500);
        
    
            var marker_7323f08686f444d5b2c4982a5de80bdf = L.marker(
                [-15.630776517958779, 37.682740274186],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_5c42c234d66e4f978b4952f0ea4c2d6e = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_7323f08686f444d5b2c4982a5de80bdf.setIcon(custom_icon_5c42c234d66e4f978b4952f0ea4c2d6e);
        
    
            var marker_15633dd4fd804133b2c3ebedd48e4c31 = L.marker(
                [-18.054506131134577, 33.170492233715805],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a8bb034321b046adbbe29034d9e3ed33 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_15633dd4fd804133b2c3ebedd48e4c31.setIcon(custom_icon_a8bb034321b046adbbe29034d9e3ed33);
        
    
            var marker_89803fbd403e47db8fbe20a9ffe9cd26 = L.marker(
                [-17.882391655739365, 36.888277839291234],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_1835def64b7f477db241ac7a7327bd2c = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_89803fbd403e47db8fbe20a9ffe9cd26.setIcon(custom_icon_1835def64b7f477db241ac7a7327bd2c);
        
    
            var marker_7ce6f04ca1e24a7dbb702104e2135434 = L.marker(
                [-19.849969795632198, 34.874005976260165],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_c99924790058460da22ccecf8d2750bd = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_7ce6f04ca1e24a7dbb702104e2135434.setIcon(custom_icon_c99924790058460da22ccecf8d2750bd);
        
    
            var marker_a7b6273245224ba3bb348e4015c66c12 = L.marker(
                [-11.82813415, 40.07479945],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_e5df2f5f7063468fb93d1116c56ac7ed = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_a7b6273245224ba3bb348e4015c66c12.setIcon(custom_icon_e5df2f5f7063468fb93d1116c56ac7ed);
        
    
            var marker_b19cf85d16704224afba9653b370e105 = L.marker(
                [-11.8282321, 40.07499935],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_2c04ece6a0e24b998e8aa86c3ba0858e = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_b19cf85d16704224afba9653b370e105.setIcon(custom_icon_2c04ece6a0e24b998e8aa86c3ba0858e);
        
    
            var marker_9d50090802ec4906aae4ef29c02aedd5 = L.marker(
                [-11.82795135, 40.074377999999996],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_04680256ae5b4de1985613e5831ba3f6 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_9d50090802ec4906aae4ef29c02aedd5.setIcon(custom_icon_04680256ae5b4de1985613e5831ba3f6);
        
    
            var marker_d67e7414851a413b832013d3948778cd = L.marker(
                [-20.204771000000004, 34.15673015],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_2a465108c1c04cfbb0edc8d954ece9e3 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_d67e7414851a413b832013d3948778cd.setIcon(custom_icon_2a465108c1c04cfbb0edc8d954ece9e3);
        
    
            var marker_8ad2e4102e6a463aa59f62d370373d5c = L.marker(
                [-19.9595375761365, 33.36068351796803],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_1ad31b4a8076468e87957754c7eb5f8b = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_8ad2e4102e6a463aa59f62d370373d5c.setIcon(custom_icon_1ad31b4a8076468e87957754c7eb5f8b);
        
    
            var marker_057c4cf13fde493983574585578d0d72 = L.marker(
                [-11.931154465976027, 40.10737505487358],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_500aa1e3c8c04724ad2430e28d8a9129 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_057c4cf13fde493983574585578d0d72.setIcon(custom_icon_500aa1e3c8c04724ad2430e28d8a9129);
        
    
            var marker_5dee9e67b21643a7be91a8304b58b072 = L.marker(
                [-15.378391163931033, 33.206878157488795],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_82a35c78187545e2a8364c6ebbd7936e = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_5dee9e67b21643a7be91a8304b58b072.setIcon(custom_icon_82a35c78187545e2a8364c6ebbd7936e);
        
    
            var marker_0010b440b2e54aec822c7a0aeacde790 = L.marker(
                [-19.7837387, 34.87908159999999],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_45ca7d45d4c247aeb8f5f637fb5f9275 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_0010b440b2e54aec822c7a0aeacde790.setIcon(custom_icon_45ca7d45d4c247aeb8f5f637fb5f9275);
        
    
            var marker_6b52fb9ab9074769a259a2115dedf0db = L.marker(
                [-19.789483559089607, 34.88527158379799],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_5c878d965e834b0189aed9bb53cb0e5a = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_6b52fb9ab9074769a259a2115dedf0db.setIcon(custom_icon_5c878d965e834b0189aed9bb53cb0e5a);
        
    
            var marker_a65ea5289728419b9259d2328bfe0940 = L.marker(
                [-19.57927473249745, 35.11946002283962],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_bb3c3a9468cf4bc4b10b3c0982fb4990 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_a65ea5289728419b9259d2328bfe0940.setIcon(custom_icon_bb3c3a9468cf4bc4b10b3c0982fb4990);
        
    
            var marker_3c69bef4d6e7489196a2c156a1641070 = L.marker(
                [-19.57470554488201, 35.22675967461576],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_25609e6af1a54ef4a1d7819db358db53 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_3c69bef4d6e7489196a2c156a1641070.setIcon(custom_icon_25609e6af1a54ef4a1d7819db358db53);
        
    
            var marker_ac560bb780d442a6864812b7e395e6ae = L.marker(
                [-16.217211, 35.62581515],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_5b7c65ed161f475193f7b881617ab0bf = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_ac560bb780d442a6864812b7e395e6ae.setIcon(custom_icon_5b7c65ed161f475193f7b881617ab0bf);
        
    
            var marker_464074e4581f4b09b61245fd6ccc362a = L.marker(
                [-16.29613732053522, 35.90989449222749],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_5b6d5ae24ef34f9385340a0b09d5d70f = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_464074e4581f4b09b61245fd6ccc362a.setIcon(custom_icon_5b6d5ae24ef34f9385340a0b09d5d70f);
        
    
            var marker_f3576f1cc26a40e1a5060af7ec9e2d11 = L.marker(
                [-16.357109483125758, 35.45536527871711],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_d28a17a74865414c9b83bc9b2467ae58 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_f3576f1cc26a40e1a5060af7ec9e2d11.setIcon(custom_icon_d28a17a74865414c9b83bc9b2467ae58);
        
    
            var marker_04ceb22462be4bbb9cb7f8f772aa4add = L.marker(
                [-16.438370863648768, 35.49959152174497],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_f2dd21f5f36948a68cee82caee013572 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_04ceb22462be4bbb9cb7f8f772aa4add.setIcon(custom_icon_f2dd21f5f36948a68cee82caee013572);
        
    
            var marker_9d24ca518b8b42d5b3093d519f6c708d = L.marker(
                [-16.31307275575145, 35.63139693571401],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_2a252a9d671945f1a955c7788ea1771b = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_9d24ca518b8b42d5b3093d519f6c708d.setIcon(custom_icon_2a252a9d671945f1a955c7788ea1771b);
        
    
            var marker_4b621aea5c5b48ab9f55a1a536b1d3fe = L.marker(
                [-25.730293887590136, 32.67311976988546],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_46e701ca9f974c0e85dbd645dac63c5a = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_4b621aea5c5b48ab9f55a1a536b1d3fe.setIcon(custom_icon_46e701ca9f974c0e85dbd645dac63c5a);
        
    
            var marker_61f0ae8799ef46429b0a9c862368515a = L.marker(
                [-25.731232694481506, 32.67329387328657],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_b0ccae8545274344868c0da91b851244 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_61f0ae8799ef46429b0a9c862368515a.setIcon(custom_icon_b0ccae8545274344868c0da91b851244);
        
    
            var marker_fe1f45a6efc0477f9995735e77467371 = L.marker(
                [-25.730836111191742, 32.672989002532915],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_c9c921758cea48f89a0071f6be04db75 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_fe1f45a6efc0477f9995735e77467371.setIcon(custom_icon_c9c921758cea48f89a0071f6be04db75);
        
    
            var marker_ffce9f80a0d04276ab243c89e71529d4 = L.marker(
                [-25.73051118513917, 32.67178435257131],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_03a969c7d16d43038daa02fa4f7f898b = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_ffce9f80a0d04276ab243c89e71529d4.setIcon(custom_icon_03a969c7d16d43038daa02fa4f7f898b);
        
    
            var marker_5ca43ab5ee3646d5a93f68bdead56954 = L.marker(
                [-19.409719796719884, 33.29411471518685],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_8e7d95f48da9466b8e8a65551090e976 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_5ca43ab5ee3646d5a93f68bdead56954.setIcon(custom_icon_8e7d95f48da9466b8e8a65551090e976);
        
    
            var marker_b63e93b302ff4369a91119f8d084e9ed = L.marker(
                [-23.8796208247523, 35.38375696460765],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_1419a6861db4463396f016a56d1b4cb8 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_b63e93b302ff4369a91119f8d084e9ed.setIcon(custom_icon_1419a6861db4463396f016a56d1b4cb8);
        
    
            var marker_9abdf34d98694efe921bdb5d608587a5 = L.marker(
                [-19.801766946972318, 34.890941557336056],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_081fe2a31ac8451f9a2a981cdd2aa3a0 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_9abdf34d98694efe921bdb5d608587a5.setIcon(custom_icon_081fe2a31ac8451f9a2a981cdd2aa3a0);
        
    
            var marker_5acce309c379496da930820ad74f1479 = L.marker(
                [-24.71413420478587, 34.74740360906775],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_2a43814a71754a4da9865a2cff59f309 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_5acce309c379496da930820ad74f1479.setIcon(custom_icon_2a43814a71754a4da9865a2cff59f309);
        
    
            var marker_1fbcd6f0ad3c4a8891c0ba7043f1159f = L.marker(
                [-17.861562087628354, 36.89521038254311],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_237894a3520b4b4d9a6ac053ea2ede4d = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_1fbcd6f0ad3c4a8891c0ba7043f1159f.setIcon(custom_icon_237894a3520b4b4d9a6ac053ea2ede4d);
        
    
            var marker_3c514af6854b4716b5f9a789a5ff1281 = L.marker(
                [-19.27139200126623, 34.20373493369942],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_9ff5d1afce7c412e93c81d08980ecfcd = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_3c514af6854b4716b5f9a789a5ff1281.setIcon(custom_icon_9ff5d1afce7c412e93c81d08980ecfcd);
        
    
            var marker_07ee16149bc24af292427452fbc69d24 = L.marker(
                [-25.89687072327935, 32.56337750656702],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_c5321111aa08467ba8c264a4bf769554 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_07ee16149bc24af292427452fbc69d24.setIcon(custom_icon_c5321111aa08467ba8c264a4bf769554);
        
    
            var marker_b6ef09ce045a4cec8a3be02e575c554b = L.marker(
                [-25.897123352038065, 32.57013967373638],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_b39dce14515d4c379d7026bc9b22d400 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_b6ef09ce045a4cec8a3be02e575c554b.setIcon(custom_icon_b39dce14515d4c379d7026bc9b22d400);
        
    
            var marker_62aa848145634aa4966d43d021ac00ec = L.marker(
                [-17.863573766666665, 36.893771838219195],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_331172cd4e274e87a229585101c0a676 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_62aa848145634aa4966d43d021ac00ec.setIcon(custom_icon_331172cd4e274e87a229585101c0a676);
        
    
            var marker_40fc3ea3a7954da39fbcae04a68afe28 = L.marker(
                [-25.859903367812795, 32.565964493975706],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a3555ba42727484496247f0189778725 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_40fc3ea3a7954da39fbcae04a68afe28.setIcon(custom_icon_a3555ba42727484496247f0189778725);
        
    
            var marker_47aead9419944372badc3d7a1747f855 = L.marker(
                [-16.22883405390653, 39.90725572129173],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ff3a034ff654416691dddceb936f8386 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_47aead9419944372badc3d7a1747f855.setIcon(custom_icon_ff3a034ff654416691dddceb936f8386);
        
    
            var marker_fcab0f3f9ea14e69a486acbc86c937dc = L.marker(
                [-16.218728406623004, 39.89905959214912],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_c139bf3cd54841a096a5c718f4de1eec = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_fcab0f3f9ea14e69a486acbc86c937dc.setIcon(custom_icon_c139bf3cd54841a096a5c718f4de1eec);
        
    
            var marker_8479844c6b7243afb6758833bdab73ac = L.marker(
                [-12.948221474445335, 40.32695921295383],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_b66a204d6b0449708a6490eb530828b8 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_8479844c6b7243afb6758833bdab73ac.setIcon(custom_icon_b66a204d6b0449708a6490eb530828b8);
        
    
            var marker_2509f56ea777489196511e72a032acba = L.marker(
                [-12.995055850000005, 40.3886345],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_54953725a293464b81361d5a712feefe = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_2509f56ea777489196511e72a032acba.setIcon(custom_icon_54953725a293464b81361d5a712feefe);
        
    
            var marker_97997fd2149a4ca596e013eb5b15896b = L.marker(
                [-12.9950071, 40.38852575000001],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_892c9f7cc3a6486e83e6753294d1af07 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_97997fd2149a4ca596e013eb5b15896b.setIcon(custom_icon_892c9f7cc3a6486e83e6753294d1af07);
        
    
            var marker_9e523afe04d241d685e7657f1c6566ba = L.marker(
                [-12.99523837575293, 40.388335812433134],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_50e7886545114a2c90c716de574c0a94 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_9e523afe04d241d685e7657f1c6566ba.setIcon(custom_icon_50e7886545114a2c90c716de574c0a94);
        
    
            var marker_b84abc1617c845478009773146d935b6 = L.marker(
                [-12.9946922803267, 40.3887881403631],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_e04d6da58ba345de9011b86299bfaee8 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_b84abc1617c845478009773146d935b6.setIcon(custom_icon_e04d6da58ba345de9011b86299bfaee8);
        
    
            var marker_f269d36024bb4ad2844b46137d613424 = L.marker(
                [-12.9950489, 40.388426800000005],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_4b2860596dc74e3b90f306d5c492fab6 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_f269d36024bb4ad2844b46137d613424.setIcon(custom_icon_4b2860596dc74e3b90f306d5c492fab6);
        
    
            var marker_c27c1fcdd96447f1aaaf24ccbb9c872f = L.marker(
                [-12.994917375560409, 40.38882761038038],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_720afd5bfb8349ffaa19ebbb5f9fd34b = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_c27c1fcdd96447f1aaaf24ccbb9c872f.setIcon(custom_icon_720afd5bfb8349ffaa19ebbb5f9fd34b);
        
    
            var marker_e9c224227d5a438bb0dc6a6d7eb43260 = L.marker(
                [-13.19722073119509, 37.49879616200989],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_9b45f120f8254ba4a2a2efac43a92134 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_e9c224227d5a438bb0dc6a6d7eb43260.setIcon(custom_icon_9b45f120f8254ba4a2a2efac43a92134);
        
    
            var marker_740291c0c8b54c72839211147a2b911b = L.marker(
                [-19.11429619768267, 33.45775978526408],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_1f9ef64bd62d433cbdbb346a7825da20 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_740291c0c8b54c72839211147a2b911b.setIcon(custom_icon_1f9ef64bd62d433cbdbb346a7825da20);
        
    
            var marker_487329b79e904d04b93586d08362f41b = L.marker(
                [-25.9065099, 32.5264641],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_6bf11915a9e64e038dcbd5af169e9f0e = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_487329b79e904d04b93586d08362f41b.setIcon(custom_icon_6bf11915a9e64e038dcbd5af169e9f0e);
        
    
            var marker_d7f8d8b7a381445ea7d6b19a96203301 = L.marker(
                [-25.912669855330854, 32.52511731355403],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_57a244b04eb246f695d84c4506859dd0 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_d7f8d8b7a381445ea7d6b19a96203301.setIcon(custom_icon_57a244b04eb246f695d84c4506859dd0);
        
    
            var marker_07c651a518494308ad9c85410b78e066 = L.marker(
                [-25.914256597744043, 32.53154799899555],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_05f90af08f5d4c2c9e1a05b3ce29c494 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_07c651a518494308ad9c85410b78e066.setIcon(custom_icon_05f90af08f5d4c2c9e1a05b3ce29c494);
        
    
            var marker_c3f78c30c17d45f8b558e27965bc4cfc = L.marker(
                [-19.724918686489417, 34.81950471457549],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_96bc68afacdc46dbbcc2c42b5e70556b = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_c3f78c30c17d45f8b558e27965bc4cfc.setIcon(custom_icon_96bc68afacdc46dbbcc2c42b5e70556b);
        
    
            var marker_481e06b7e84a418cb06194efc1e72357 = L.marker(
                [-11.812900371478719, 40.10730798739528],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_88aac31c584c4d35b1ca6f27db9909db = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_481e06b7e84a418cb06194efc1e72357.setIcon(custom_icon_88aac31c584c4d35b1ca6f27db9909db);
        
    
            var marker_42c72a35330b4560a58150734db1367d = L.marker(
                [-14.802288703131172, 36.533570042668174],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_4c5d75383f4544e485b26947fd84dcbe = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_42c72a35330b4560a58150734db1367d.setIcon(custom_icon_4c5d75383f4544e485b26947fd84dcbe);
        
    
            var marker_9332bd93f62e423cb7872dafac296fa9 = L.marker(
                [-26.013312834869406, 32.41852933174087],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_672f9637635849a192582e4db5ca06f3 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_9332bd93f62e423cb7872dafac296fa9.setIcon(custom_icon_672f9637635849a192582e4db5ca06f3);
        
    
            var marker_e2c3d24ac9654943bb2516183c08ef82 = L.marker(
                [-25.725050650000004, 32.65454905],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_7383340ecc9248a1ad99fb9cc7db9471 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_e2c3d24ac9654943bb2516183c08ef82.setIcon(custom_icon_7383340ecc9248a1ad99fb9cc7db9471);
        
    
            var marker_41ca2dae19224968bb8a935b494ffc9d = L.marker(
                [-14.798090634424685, 36.547906599315816],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_73fe8ce0e0ed45ec807202e58cbda04e = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_41ca2dae19224968bb8a935b494ffc9d.setIcon(custom_icon_73fe8ce0e0ed45ec807202e58cbda04e);
        
    
            var marker_27ae3a2fdf3e4d1db35b5208640f54fd = L.marker(
                [-15.73956163553483, 32.76925435642922],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_8e211ad1605647df99f8cf1fd9f78e12 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_27ae3a2fdf3e4d1db35b5208640f54fd.setIcon(custom_icon_8e211ad1605647df99f8cf1fd9f78e12);
        
    
            var marker_7b2d1a0e0b9442e3a963ab9c1a997fab = L.marker(
                [-15.740167370110656, 32.76961709235178],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_4c36c6e44dd14a6f8d842a4d02ec8d7a = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_7b2d1a0e0b9442e3a963ab9c1a997fab.setIcon(custom_icon_4c36c6e44dd14a6f8d842a4d02ec8d7a);
        
    
            var marker_a394cc2496d744e6912e80411e8327e7 = L.marker(
                [-15.739495722230558, 32.768679116876044],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_7baee4bf9949439ab2bf08d4b9839c45 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_a394cc2496d744e6912e80411e8327e7.setIcon(custom_icon_7baee4bf9949439ab2bf08d4b9839c45);
        
    
            var marker_ff43516e549d47889b018689fbc7c049 = L.marker(
                [-15.741002670127637, 32.76786728509906],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_e2c055de67d64544a64aca365098ce83 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_ff43516e549d47889b018689fbc7c049.setIcon(custom_icon_e2c055de67d64544a64aca365098ce83);
        
    
            var marker_9c5388ab74fb455f9dce74d7391348f6 = L.marker(
                [-16.633532000000002, 35.172801500000006],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_d42b865a7d4748b29426417e4c66bcbe = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_9c5388ab74fb455f9dce74d7391348f6.setIcon(custom_icon_d42b865a7d4748b29426417e4c66bcbe);
        
    
            var marker_b97ea81470314643ae6139170ace9030 = L.marker(
                [-22.25241812523343, 35.111901046672365],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_9ce7cf479f144c7c9c559d2280ce619d = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_b97ea81470314643ae6139170ace9030.setIcon(custom_icon_9ce7cf479f144c7c9c559d2280ce619d);
        
    
            var marker_6339b0f84d30429b9fac9cedb9f28cad = L.marker(
                [-12.982447418561538, 40.546053552942944],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_e7681adc23664d2fae27635c845339bb = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_6339b0f84d30429b9fac9cedb9f28cad.setIcon(custom_icon_e7681adc23664d2fae27635c845339bb);
        
    
            var marker_3eeb80d30e99409a98fb2b19d966a87f = L.marker(
                [-12.435358691522024, 40.4889655441181],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_4f7181ea1bba41a99a1a57c2869e5f93 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_3eeb80d30e99409a98fb2b19d966a87f.setIcon(custom_icon_4f7181ea1bba41a99a1a57c2869e5f93);
        
    
            var marker_ac7b35051cf64520b209933b76c60aad = L.marker(
                [-25.90561303381738, 32.567292815090276],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ea02ec83f5aa4070897c69664e5e5a78 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_ac7b35051cf64520b209933b76c60aad.setIcon(custom_icon_ea02ec83f5aa4070897c69664e5e5a78);
        
    
            var marker_d91caa5eab3e4f55be8292b578040979 = L.marker(
                [-19.903286250000004, 33.31850645],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_e9e0017b8d79486e8c95e6a12a8a475e = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_d91caa5eab3e4f55be8292b578040979.setIcon(custom_icon_e9e0017b8d79486e8c95e6a12a8a475e);
        
    
            var marker_376505bdc6ca442c83ddbb867752bd02 = L.marker(
                [-19.835749156994638, 34.88440529719475],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_0b863b69588c4a5f871e5ebb0f288468 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_376505bdc6ca442c83ddbb867752bd02.setIcon(custom_icon_0b863b69588c4a5f871e5ebb0f288468);
        
    
            var marker_277cfc5186854c25b3698c9396abc07c = L.marker(
                [-19.812835040147263, 34.86372276349208],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_051e1c62a0ff4d15869b26ab6d058998 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_277cfc5186854c25b3698c9396abc07c.setIcon(custom_icon_051e1c62a0ff4d15869b26ab6d058998);
        
    
            var marker_6897427c7e97480dbff8e673edc4974c = L.marker(
                [-19.767557065645846, 34.869174792449655],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_3da1564a887242ccb6695c380507f4e1 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_6897427c7e97480dbff8e673edc4974c.setIcon(custom_icon_3da1564a887242ccb6695c380507f4e1);
        
    
            var marker_5d4d19f961d643c9b82d0138d6522e39 = L.marker(
                [-13.382290044298742, 39.78153116467058],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_9be785ffae5c4d66822aec59eb25d72f = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_5d4d19f961d643c9b82d0138d6522e39.setIcon(custom_icon_9be785ffae5c4d66822aec59eb25d72f);
        
    
            var marker_676ca599c7a74f378650014a3bfbcf84 = L.marker(
                [-12.985670101173552, 40.53765768603249],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a2df36f922d64a7f82f27a21d0ee3142 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_676ca599c7a74f378650014a3bfbcf84.setIcon(custom_icon_a2df36f922d64a7f82f27a21d0ee3142);
        
    
            var marker_a2a04c01a4094014a57907074aee86bf = L.marker(
                [-14.16669365, 39.17114105000001],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_37f0b805ea814364969caadb25ae1798 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_a2a04c01a4094014a57907074aee86bf.setIcon(custom_icon_37f0b805ea814364969caadb25ae1798);
        
    
            var marker_db70700585d245f19cc7076520b49519 = L.marker(
                [-14.390813231293484, 40.07900881031924],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_332e4f20c1f54586a97080a7e747051c = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_db70700585d245f19cc7076520b49519.setIcon(custom_icon_332e4f20c1f54586a97080a7e747051c);
        
    
            var marker_05280678d07d42d594f18010dfc100b2 = L.marker(
                [-16.639303451846104, 39.496034665988766],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_1a946349995a4e79a4776fad5fa2ef04 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_05280678d07d42d594f18010dfc100b2.setIcon(custom_icon_1a946349995a4e79a4776fad5fa2ef04);
        
    
            var marker_a358ccfec7fc456e9959b5ffcd6568a5 = L.marker(
                [-14.892574420600027, 37.770672542234614],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_10d536641f9d43d6808abd53a72a18b2 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_a358ccfec7fc456e9959b5ffcd6568a5.setIcon(custom_icon_10d536641f9d43d6808abd53a72a18b2);
        
    
            var marker_bcecc53a51cf46a782eaf21d5058bb00 = L.marker(
                [-14.716817462312044, 37.834792778600544],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_b8450d03aea84789aa74dc0612531235 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_bcecc53a51cf46a782eaf21d5058bb00.setIcon(custom_icon_b8450d03aea84789aa74dc0612531235);
        
    
            var marker_2c66b7e5f8cc4808ad4e778c8f0e910d = L.marker(
                [-14.939281158187095, 38.689471625664126],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_cfbef24b5c144471acf4bd52ae192482 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_2c66b7e5f8cc4808ad4e778c8f0e910d.setIcon(custom_icon_cfbef24b5c144471acf4bd52ae192482);
        
    
            var marker_a7ec624967bf4511b4add6177022154c = L.marker(
                [-15.100927412996207, 38.229826710514665],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_31537d2ca622492288bb1691901b18bd = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_a7ec624967bf4511b4add6177022154c.setIcon(custom_icon_31537d2ca622492288bb1691901b18bd);
        
    
            var marker_e27af1ae55ae4f9fb8ace424eedc89d1 = L.marker(
                [-15.003337599999996, 37.7635848],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_f8dacdbc0097435bb169a3bbef80f59d = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_e27af1ae55ae4f9fb8ace424eedc89d1.setIcon(custom_icon_f8dacdbc0097435bb169a3bbef80f59d);
        
    
            var marker_fefb6fc184014aee9fedfdfb25fe1957 = L.marker(
                [-14.76560885, 39.788471200000004],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_8568ff3ee7bc47b7ab4a1c6db7f5e361 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_fefb6fc184014aee9fedfdfb25fe1957.setIcon(custom_icon_8568ff3ee7bc47b7ab4a1c6db7f5e361);
        
    
            var marker_38595afded8444f6a42d68ecc70d090d = L.marker(
                [-13.12788349301426, 35.17573492501526],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_24eb3753378048c8963f430dd1c5ba1c = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_38595afded8444f6a42d68ecc70d090d.setIcon(custom_icon_24eb3753378048c8963f430dd1c5ba1c);
        
    
            var marker_f36047752ab04610af215b0951a5f854 = L.marker(
                [-14.247551249999999, 35.62493185],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_9d0b99564a7147c986e951f3f859cb77 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_f36047752ab04610af215b0951a5f854.setIcon(custom_icon_9d0b99564a7147c986e951f3f859cb77);
        
    
            var marker_96b989d90f5149b1a86da02762795768 = L.marker(
                [-14.988071218337458, 35.89195409899272],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_bd55f69a95924e09bd39ff6ba1c50559 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_96b989d90f5149b1a86da02762795768.setIcon(custom_icon_bd55f69a95924e09bd39ff6ba1c50559);
        
    
            var marker_460447ee2a8d44369227e5e857726e5c = L.marker(
                [-13.615033, 35.25648339999999],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_e6e07276aa694c25ba1139c33a1ee8a8 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_460447ee2a8d44369227e5e857726e5c.setIcon(custom_icon_e6e07276aa694c25ba1139c33a1ee8a8);
        
    
            var marker_07d570d22ab841e39fed8dca679d6f88 = L.marker(
                [-15.198811476875958, 36.70232407497749],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_ee083edbc90342fb80c88ca17f759235 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_07d570d22ab841e39fed8dca679d6f88.setIcon(custom_icon_ee083edbc90342fb80c88ca17f759235);
        
    
            var marker_a8e4850a53284ddf91db948e1598184e = L.marker(
                [-17.894701512182895, 36.766468658734205],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_39458ff4e79f4f7faac4d7574841a6c1 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_a8e4850a53284ddf91db948e1598184e.setIcon(custom_icon_39458ff4e79f4f7faac4d7574841a6c1);
        
    
            var marker_9624d068f4e1424683f9b9c61491cd24 = L.marker(
                [-16.428435795849627, 36.745525640242384],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_57417286559640a4b9a1fd2d28596039 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_9624d068f4e1424683f9b9c61491cd24.setIcon(custom_icon_57417286559640a4b9a1fd2d28596039);
        
    
            var marker_9fddddc2febe4e28b3aceb8c8d4c8cfa = L.marker(
                [-15.028961169938885, 38.04749330679614],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_6d9d337352c64c16937ad4bf492f6487 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_9fddddc2febe4e28b3aceb8c8d4c8cfa.setIcon(custom_icon_6d9d337352c64c16937ad4bf492f6487);
        
    
            var marker_9bf33f6978f9425bb4b4900a998e45a9 = L.marker(
                [-16.19141239811908, 33.630879818335565],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_a63d121c071d4f749166acffad1a7738 = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_9bf33f6978f9425bb4b4900a998e45a9.setIcon(custom_icon_a63d121c071d4f749166acffad1a7738);
        
    
            var marker_09bf058c7f52463485b0c9299a1fbe9a = L.marker(
                [-16.12456364730406, 33.74558171122827],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_c789796f0bfd4d86a3f1a356945ee75f = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_09bf058c7f52463485b0c9299a1fbe9a.setIcon(custom_icon_c789796f0bfd4d86a3f1a356945ee75f);
        
    
            var marker_10f97a6d659e4bf8b9f6be7a2dffc176 = L.marker(
                [-16.11877396623281, 33.73054801123061],
                {}
            ).addTo(map_f36c66056d4d43709c3d5f32961f15c8);
        
    
        var custom_icon_5d4503ae9f6a41b49be6184d4e52526a = L.icon({"iconSize": [14, 14], "iconUrl": "https://nataliethurlby.github.io/useful_flood_data/icons/health_facility.svg"});
        marker_10f97a6d659e4bf8b9f6be7a2dffc176.setIcon(custom_icon_5d4503ae9f6a41b49be6184d4e52526a);
        
</script>