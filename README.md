# weather-platform
App to get an analyze weather


{
  "@context": [
    "https://geojson.org/geojson-ld/geojson-context.jsonld",
    {
      "@version": "1.1",
      "wx": "https://api.weather.gov/ontology#",
      "s": "https://schema.org/",
      "geo": "http://www.opengis.net/ont/geosparql#",
      "unit": "http://codes.wmo.int/common/unit/",
      "@vocab": "https://api.weather.gov/ontology#",
      "geometry": {
        "@id": "s:GeoCoordinates",
        "@type": "geo:wktLiteral"
      },
      "city": "s:addressLocality",
      "state": "s:addressRegion",
      "distance": {
        "@id": "s:Distance",
        "@type": "s:QuantitativeValue"
      },
      "bearing": {
        "@type": "s:QuantitativeValue"
      },
      "value": {
        "@id": "s:value"
      },
      "unitCode": {
        "@id": "s:unitCode",
        "@type": "@id"
      },
      "forecastOffice": {
        "@type": "@id"
      },
      "forecastGridData": {
        "@type": "@id"
      },
      "publicZone": {
        "@type": "@id"
      },
      "county": {
        "@type": "@id"
      },
      "observationStations": {
        "@container": "@list",
        "@type": "@id"
      }
    }
  ],
  "type": "FeatureCollection",
  "features": [
    {
      "id": "https://api.weather.gov/stations/KFFO",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -84.05,
          39.83333
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KFFO",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 250.8504
        },
        "stationIdentifier": "KFFO",
        "name": "Dayton / Wright-Patterson Air Force Base",
        "timeZone": "America/New_York",
        "provider": "OTHER-MTR",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 14822.984988175
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 61
        },
        "forecast": "https://api.weather.gov/zones/forecast/OHZ062",
        "county": "https://api.weather.gov/zones/county/OHC057",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/OHZ062"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KDAY",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -84.21861,
          39.90611
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KDAY",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 306.9336
        },
        "stationIdentifier": "KDAY",
        "name": "Dayton, Cox Dayton International Airport",
        "timeZone": "America/New_York",
        "provider": "ASOS-HFM",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 15331.860385359
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 354
        },
        "forecast": "https://api.weather.gov/zones/forecast/OHZ061",
        "county": "https://api.weather.gov/zones/county/OHC113",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/OHZ061"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KGDK",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -83.99278,
          39.69072
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KGDK",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 289.2552
        },
        "stationIdentifier": "KGDK",
        "name": "Greene County - Lewis A Jackson Regional Airport",
        "timeZone": "America/New_York",
        "provider": "",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 19876.986844923
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 115
        },
        "forecast": "https://api.weather.gov/zones/forecast/OHZ062",
        "county": "https://api.weather.gov/zones/county/OHC057",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/OHZ062"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KMGY",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -84.22472,
          39.58889
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KMGY",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 291.9984
        },
        "stationIdentifier": "KMGY",
        "name": "Dayton, Dayton-Wright Brothers Airport",
        "timeZone": "America/New_York",
        "provider": "ASOS-HFM",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 20103.856285752
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 185
        },
        "forecast": "https://api.weather.gov/zones/forecast/OHZ061",
        "county": "https://api.weather.gov/zones/county/OHC113",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/OHZ061"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KSGH",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -83.84,
          39.84028
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KSGH",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 320.04
        },
        "stationIdentifier": "KSGH",
        "name": "Springfield, Springfield-Beckley Municipal Airport",
        "timeZone": "America/New_York",
        "provider": "ASOS-HFM",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 31915.332880167
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 75
        },
        "forecast": "https://api.weather.gov/zones/forecast/OHZ053",
        "county": "https://api.weather.gov/zones/county/OHC023",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/OHZ053"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KI68",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -84.25184,
          39.46217
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KI68",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 301.4472
        },
        "stationIdentifier": "KI68",
        "name": "Warren County Airport",
        "timeZone": "America/New_York",
        "provider": "OTHER-MTR",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 34366.806576924
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 187
        },
        "forecast": "https://api.weather.gov/zones/forecast/OHZ071",
        "county": "https://api.weather.gov/zones/county/OHC165",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/OHZ071"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KILN",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -83.77917,
          39.42833
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KILN",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 327.9648
        },
        "stationIdentifier": "KILN",
        "name": "Wilmington, Airborne Airpark Airport",
        "timeZone": "America/New_York",
        "provider": "ASOS-HFM",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 52392.975892974
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 136
        },
        "forecast": "https://api.weather.gov/zones/forecast/OHZ072",
        "county": "https://api.weather.gov/zones/county/OHC027",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/OHZ072"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KHAO",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -84.52061,
          39.36121
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KHAO",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 185.0136
        },
        "stationIdentifier": "KHAO",
        "name": "Butler County Regional Airport",
        "timeZone": "America/New_York",
        "provider": "ASOS-HFM",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 52924.295579922
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 211
        },
        "forecast": "https://api.weather.gov/zones/forecast/OHZ070",
        "county": "https://api.weather.gov/zones/county/OHC017",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/OHZ070"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KRID",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -84.8428,
          39.7572
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KRID",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 347.472
        },
        "stationIdentifier": "KRID",
        "name": "Richmond Municipal Airport",
        "timeZone": "America/Indiana/Indianapolis",
        "provider": "NonFedAWOS",
        "subProvider": "TG",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 54800.444854879
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 268
        },
        "forecast": "https://api.weather.gov/zones/forecast/INZ050",
        "county": "https://api.weather.gov/zones/county/INC177",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/INZ050"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KI74",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -83.7534,
          40.1326
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KI74",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 325.2216
        },
        "stationIdentifier": "KI74",
        "name": "Urbana Grimes Field",
        "timeZone": "America/New_York",
        "provider": "NonFedAWOS",
        "subProvider": "TG",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 55654.569060025
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 43
        },
        "forecast": "https://api.weather.gov/zones/forecast/OHZ052",
        "county": "https://api.weather.gov/zones/county/OHC021",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/OHZ052"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KVES",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -84.5319,
          40.2044
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KVES",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 306.9336
        },
        "stationIdentifier": "KVES",
        "name": "Versailles Darke County Airport",
        "timeZone": "America/New_York",
        "provider": "OTHER-MTR",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 56004.143911411
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 329
        },
        "forecast": "https://api.weather.gov/zones/forecast/OHZ042",
        "county": "https://api.weather.gov/zones/county/OHC037",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/OHZ042"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KOXD",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -84.78436,
          39.50225
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KOXD",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 317.2968
        },
        "stationIdentifier": "KOXD",
        "name": "Miami University Airport",
        "timeZone": "America/New_York",
        "provider": "NonFedAWOS",
        "subProvider": "TG",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 58024.785018655
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 239
        },
        "forecast": "https://api.weather.gov/zones/forecast/OHZ070",
        "county": "https://api.weather.gov/zones/county/OHC017",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/OHZ070"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KUYF",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -83.462,
          39.9327
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KUYF",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 330.0984
        },
        "stationIdentifier": "KUYF",
        "name": "London Madison County Airport",
        "timeZone": "America/New_York",
        "provider": "OTHER-MTR",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 65734.062243163
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 73
        },
        "forecast": "https://api.weather.gov/zones/forecast/OHZ054",
        "county": "https://api.weather.gov/zones/county/OHC097",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/OHZ054"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KI23",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -83.4205,
          39.5704
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KI23",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 298.704
        },
        "stationIdentifier": "KI23",
        "name": "Fayette County Airport",
        "timeZone": "America/New_York",
        "provider": "NonFedAWOS",
        "subProvider": "TG",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 70422.193073734
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 108
        },
        "forecast": "https://api.weather.gov/zones/forecast/OHZ063",
        "county": "https://api.weather.gov/zones/county/OHC047",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/OHZ063"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KEDJ",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -83.8192,
          40.3723
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KEDJ",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 341.9856
        },
        "stationIdentifier": "KEDJ",
        "name": "Bellefontaine Regional Airport",
        "timeZone": "America/New_York",
        "provider": "OTHER-MTR",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 74585.335235492
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 25
        },
        "forecast": "https://api.weather.gov/zones/forecast/OHZ044",
        "county": "https://api.weather.gov/zones/county/OHC091",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/OHZ044"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KI67",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -84.7743,
          39.2589
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KI67",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 178.0032
        },
        "stationIdentifier": "KI67",
        "name": "Cincinnati W Airport",
        "timeZone": "America/New_York",
        "provider": "OTHER-MTR",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 75009.991570291
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 221
        },
        "forecast": "https://api.weather.gov/zones/forecast/OHZ077",
        "county": "https://api.weather.gov/zones/county/OHC061",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/OHZ077"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KLUK",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -84.41583,
          39.10583
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KLUK",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 146.9136
        },
        "stationIdentifier": "KLUK",
        "name": "Cincinnati, Cincinnati Municipal Airport Lunken Field",
        "timeZone": "America/New_York",
        "provider": "ASOS-HFM",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 75977.909557753
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 194
        },
        "forecast": "https://api.weather.gov/zones/forecast/OHZ077",
        "county": "https://api.weather.gov/zones/county/OHC061",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/OHZ077"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KI69",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -84.2102,
          39.0784
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KI69",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 256.9464
        },
        "stationIdentifier": "KI69",
        "name": "Batavia Clermont County Airport",
        "timeZone": "America/New_York",
        "provider": "OTHER-MTR",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 76775.693131865
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 180
        },
        "forecast": "https://api.weather.gov/zones/forecast/OHZ078",
        "county": "https://api.weather.gov/zones/county/OHC025",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/OHZ078"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KAXV",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -84.29808,
          40.49356
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KAXV",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 277.9776
        },
        "stationIdentifier": "KAXV",
        "name": "Neil Armstrong Airport",
        "timeZone": "America/New_York",
        "provider": "OTHER-MTR",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 81000.675665651
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 354
        },
        "forecast": "https://api.weather.gov/zones/forecast/OHZ035",
        "county": "https://api.weather.gov/zones/county/OHC011",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/OHZ035"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KMRT",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -83.3516,
          40.2247
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KMRT",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 311.2008
        },
        "stationIdentifier": "KMRT",
        "name": "Marysville Union County Airport",
        "timeZone": "America/New_York",
        "provider": "OTHER-MTR",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 88403.857721703
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 54
        },
        "forecast": "https://api.weather.gov/zones/forecast/OHZ045",
        "county": "https://api.weather.gov/zones/county/OHC159",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/OHZ045"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KCVG",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -84.67229,
          39.04456
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KCVG",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 262.128
        },
        "stationIdentifier": "KCVG",
        "name": "Cincinnati/Northern Kentucky International Airport",
        "timeZone": "America/New_York",
        "provider": "ASOS-HFM",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 90108.148383934
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 206
        },
        "forecast": "https://api.weather.gov/zones/forecast/KYZ091",
        "county": "https://api.weather.gov/zones/county/KYC015",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/KYZ091"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KTZR",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -83.13722,
          39.90083
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KTZR",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 276.1488
        },
        "stationIdentifier": "KTZR",
        "name": "Columbus, Bolton Field Airport",
        "timeZone": "America/New_York",
        "provider": "OTHER-MTR",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 92081.400699324
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 80
        },
        "forecast": "https://api.weather.gov/zones/forecast/OHZ055",
        "county": "https://api.weather.gov/zones/county/OHC049",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/OHZ055"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KOSU",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -83.07806,
          40.07806
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KOSU",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 274.9296
        },
        "stationIdentifier": "KOSU",
        "name": "Columbus, Ohio State University Airport",
        "timeZone": "America/New_York",
        "provider": "ASOS-HFM",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 101813.24966272
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 69
        },
        "forecast": "https://api.weather.gov/zones/forecast/OHZ055",
        "county": "https://api.weather.gov/zones/county/OHC049",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/OHZ055"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KI95",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -83.64426,
          40.61009
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KI95",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 313.6392
        },
        "stationIdentifier": "KI95",
        "name": "Hardin County Airport",
        "timeZone": "America/New_York",
        "provider": "",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 104850.75940215
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 26
        },
        "forecast": "https://api.weather.gov/zones/forecast/OHZ026",
        "county": "https://api.weather.gov/zones/county/OHC065",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/OHZ026"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KAOH",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -84.02139,
          40.70806
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KAOH",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 296.8752
        },
        "stationIdentifier": "KAOH",
        "name": "Lima, Lima Allen County Airport",
        "timeZone": "America/New_York",
        "provider": "ASOS-HFM",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 105555.12103081
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 8
        },
        "forecast": "https://api.weather.gov/zones/forecast/OHZ025",
        "county": "https://api.weather.gov/zones/county/OHC003",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/OHZ025"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KRZT",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -83.0231,
          39.4404
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KRZT",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 220.98
        },
        "stationIdentifier": "KRZT",
        "name": "Chillicothe Ross County Airport",
        "timeZone": "America/New_York",
        "provider": "OTHER-MTR",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 107384.91160083
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 109
        },
        "forecast": "https://api.weather.gov/zones/forecast/OHZ073",
        "county": "https://api.weather.gov/zones/county/OHC141",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/OHZ073"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KLCK",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -82.93333,
          39.81667
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KLCK",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 227.076
        },
        "stationIdentifier": "KLCK",
        "name": "Rickenbacker Air National Guard Base",
        "timeZone": "America/New_York",
        "provider": "OTHER-MTR",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 108509.90026511
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 86
        },
        "forecast": "https://api.weather.gov/zones/forecast/OHZ055",
        "county": "https://api.weather.gov/zones/county/OHC049",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/OHZ055"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KDLZ",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -83.1148,
          40.2797
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KDLZ",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 288.036
        },
        "stationIdentifier": "KDLZ",
        "name": "Delaware Municipal Airport",
        "timeZone": "America/New_York",
        "provider": "OTHER-MTR",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 108602.43357774
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 58
        },
        "forecast": "https://api.weather.gov/zones/forecast/OHZ046",
        "county": "https://api.weather.gov/zones/county/OHC041",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/OHZ046"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KMIE",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -85.39361,
          40.23417
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KMIE",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 284.988
        },
        "stationIdentifier": "KMIE",
        "name": "Muncie, Delaware County-Johnson Field",
        "timeZone": "America/Indiana/Indianapolis",
        "provider": "ASOS-HFM",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 113937.74083063
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 297
        },
        "forecast": "https://api.weather.gov/zones/forecast/INZ041",
        "county": "https://api.weather.gov/zones/county/INC035",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/INZ041"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KCMH",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -82.87691,
          39.9907
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KCMH",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 245.9736
        },
        "stationIdentifier": "KCMH",
        "name": "John Glenn Columbus International Airport",
        "timeZone": "America/New_York",
        "provider": "ASOS-HFM",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 115716.70905621
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 77
        },
        "forecast": "https://api.weather.gov/zones/forecast/OHZ055",
        "county": "https://api.weather.gov/zones/county/OHC049",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/OHZ055"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KAID",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -85.60977,
          40.10612
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KAID",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 276.1488
        },
        "stationIdentifier": "KAID",
        "name": "Anderson Municipal Airport",
        "timeZone": "America/Indiana/Indianapolis",
        "provider": "NonFedAWOS",
        "subProvider": "TG",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 125757.86634883
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 287
        },
        "forecast": "https://api.weather.gov/zones/forecast/INZ040",
        "county": "https://api.weather.gov/zones/county/INC095",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/INZ040"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KLHQ",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -82.66333,
          39.75722
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KLHQ",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 263.9568
        },
        "stationIdentifier": "KLHQ",
        "name": "Lancaster, Fairfield County Airport",
        "timeZone": "America/New_York",
        "provider": "ASOS-HFM",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 131510.20262295
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 90
        },
        "forecast": "https://api.weather.gov/zones/forecast/OHZ065",
        "county": "https://api.weather.gov/zones/county/OHC045",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/OHZ065"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KMNN",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -83.06833,
          40.61667
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KMNN",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 302.9712
        },
        "stationIdentifier": "KMNN",
        "name": "Marion, Marion Municipal Airport",
        "timeZone": "America/New_York",
        "provider": "ASOS-HFM",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 134748.70870274
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 45
        },
        "forecast": "https://api.weather.gov/zones/forecast/OHZ036",
        "county": "https://api.weather.gov/zones/county/OHC101",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/OHZ036"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KGEZ",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -85.79982,
          39.58546
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KGEZ",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 244.1448
        },
        "stationIdentifier": "KGEZ",
        "name": "Shelbyville Municipal Airport",
        "timeZone": "America/Indiana/Indianapolis",
        "provider": "ASOS-HFM",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 138266.71633866
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 262
        },
        "forecast": "https://api.weather.gov/zones/forecast/INZ056",
        "county": "https://api.weather.gov/zones/county/INC145",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/INZ056"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KFGX",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -83.7434,
          38.5418
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KFGX",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 277.9776
        },
        "stationIdentifier": "KFGX",
        "name": "Flemingsburg Fleming-Mason Airport",
        "timeZone": "America/New_York",
        "provider": "OTHER-MTR",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 142049.98316394
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 163
        },
        "forecast": "https://api.weather.gov/zones/forecast/KYZ099",
        "county": "https://api.weather.gov/zones/county/KYC161",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/KYZ099"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KFDY",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -83.66861,
          41.01361
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KFDY",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 248.1072
        },
        "stationIdentifier": "KFDY",
        "name": "Findlay, Findlay Airport",
        "timeZone": "America/New_York",
        "provider": "ASOS-HFM",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 145593.58901596
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 17
        },
        "forecast": "https://api.weather.gov/zones/forecast/OHZ017",
        "county": "https://api.weather.gov/zones/county/OHC063",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/OHZ017"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KVTA",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -82.4625,
          40.02278
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KVTA",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 269.1384
        },
        "stationIdentifier": "KVTA",
        "name": "Newark, Newark Heath Airport",
        "timeZone": "America/New_York",
        "provider": "ASOS-HFM",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 151044.73379504
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 78
        },
        "forecast": "https://api.weather.gov/zones/forecast/OHZ056",
        "county": "https://api.weather.gov/zones/county/OHC089",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/OHZ056"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KBAK",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -85.9,
          39.26667
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KBAK",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 199.9488
        },
        "stationIdentifier": "KBAK",
        "name": "Columbus / Bakalar",
        "timeZone": "America/Indiana/Indianapolis",
        "provider": "OTHER-MTR",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 155997.5017293
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 249
        },
        "forecast": "https://api.weather.gov/zones/forecast/INZ064",
        "county": "https://api.weather.gov/zones/county/INC005",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/INZ064"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KFWA",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -85.20637,
          40.97251
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KFWA",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 242.9256
        },
        "stationIdentifier": "KFWA",
        "name": "Fort Wayne International Airport",
        "timeZone": "America/Indiana/Indianapolis",
        "provider": "ASOS-HFM",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 158603.19630228
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 327
        },
        "forecast": "https://api.weather.gov/zones/forecast/INZ018",
        "county": "https://api.weather.gov/zones/county/INC003",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/INZ018"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KIND",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -86.2816,
          39.72518
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KIND",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 240.792
        },
        "stationIdentifier": "KIND",
        "name": "Indianapolis International Airport",
        "timeZone": "America/Indiana/Indianapolis",
        "provider": "ASOS-HFM",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 177870.6873613
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 269
        },
        "forecast": "https://api.weather.gov/zones/forecast/INZ047",
        "county": "https://api.weather.gov/zones/county/INC097",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/INZ047"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KEYE",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -86.29583,
          39.825
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KEYE",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 249.936
        },
        "stationIdentifier": "KEYE",
        "name": "Indianapolis, Eagle Creek Airpark",
        "timeZone": "America/Indiana/Indianapolis",
        "provider": "ASOS-HFM",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 179000.20264253
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 272
        },
        "forecast": "https://api.weather.gov/zones/forecast/INZ047",
        "county": "https://api.weather.gov/zones/county/INC097",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/INZ047"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KMFD",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -82.51778,
          40.82028
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KMFD",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 395.0208
        },
        "stationIdentifier": "KMFD",
        "name": "Mansfield - Mansfield Lahm Regional Airport",
        "timeZone": "America/New_York",
        "provider": "ASOS-HFM",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 184572.78576796
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 50
        },
        "forecast": "https://api.weather.gov/zones/forecast/OHZ029",
        "county": "https://api.weather.gov/zones/county/OHC139",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/OHZ029"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KFFT",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -84.90333,
          38.18472
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KFFT",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 245.0592
        },
        "stationIdentifier": "KFFT",
        "name": "Frankfort, Capital City Airport",
        "timeZone": "America/New_York",
        "provider": "ASOS",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 186288.44155652
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 199
        },
        "forecast": "https://api.weather.gov/zones/forecast/KYZ035",
        "county": "https://api.weather.gov/zones/county/KYC073",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/KYZ035"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KLEX",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -84.61146,
          38.0339
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KLEX",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 291.084
        },
        "stationIdentifier": "KLEX",
        "name": "Lexington Blue Grass Airport",
        "timeZone": "America/New_York",
        "provider": "ASOS-HFM",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 196144.17124919
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 190
        },
        "forecast": "https://api.weather.gov/zones/forecast/KYZ041",
        "county": "https://api.weather.gov/zones/county/KYC067",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/KYZ041"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KZZV",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -81.89315,
          39.94609
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KZZV",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 274.32
        },
        "stationIdentifier": "KZZV",
        "name": "Zanesville Municipal Airport",
        "timeZone": "America/New_York",
        "provider": "ASOS-HFM",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 198043.50171019
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 83
        },
        "forecast": "https://api.weather.gov/zones/forecast/OHZ057",
        "county": "https://api.weather.gov/zones/county/OHC119",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/OHZ057"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KHTS",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -82.555,
          38.365
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KHTS",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 252.0696
        },
        "stationIdentifier": "KHTS",
        "name": "Huntington, Tri-State Airport",
        "timeZone": "America/New_York",
        "provider": "ASOS-HFM",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 211134.5182304
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 137
        },
        "forecast": "https://api.weather.gov/zones/forecast/WVZ005",
        "county": "https://api.weather.gov/zones/county/WVC099",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/WVZ005"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KLOU",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -85.66361,
          38.22778
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KLOU",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 166.116
        },
        "stationIdentifier": "KLOU",
        "name": "Louisville, Bowman Field Airport",
        "timeZone": "America/Kentucky/Louisville",
        "provider": "ASOS-HFM",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 212877.8296192
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 216
        },
        "forecast": "https://api.weather.gov/zones/forecast/KYZ030",
        "county": "https://api.weather.gov/zones/county/KYC111",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/KYZ030"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KSDF",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -85.7365,
          38.17406
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KSDF",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 152.4
        },
        "stationIdentifier": "KSDF",
        "name": "Louisville Muhammad Ali International Airport",
        "timeZone": "America/Kentucky/Louisville",
        "provider": "ASOS-HFM",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 221457.96720083
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 217
        },
        "forecast": "https://api.weather.gov/zones/forecast/KYZ030",
        "county": "https://api.weather.gov/zones/county/KYC111",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/KYZ030"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KBJJ",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -81.88667,
          40.87306
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KBJJ",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 345.948
        },
        "stationIdentifier": "KBJJ",
        "name": "Wooster, Wayne County Airport",
        "timeZone": "America/New_York",
        "provider": "ASOS-HFM",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 231506.45185003
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 57
        },
        "forecast": "https://api.weather.gov/zones/forecast/OHZ031",
        "county": "https://api.weather.gov/zones/county/OHC169",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/OHZ031"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KPKB",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -81.43917,
          39.345
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KPKB",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 262.128
        },
        "stationIdentifier": "KPKB",
        "name": "Parkersburg, Mid-Ohio Valley Regional Airport",
        "timeZone": "America/New_York",
        "provider": "ASOS-HFM",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 241478.67046656
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 100
        },
        "forecast": "https://api.weather.gov/zones/forecast/WVZ009",
        "county": "https://api.weather.gov/zones/county/WVC107",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/WVZ009"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KPHD",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -81.42178,
          40.47032
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KPHD",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 272.4912
        },
        "stationIdentifier": "KPHD",
        "name": "Harry Clever Field Airport",
        "timeZone": "America/New_York",
        "provider": "ASOS-HFM",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 248915.51234174
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 70
        },
        "forecast": "https://api.weather.gov/zones/forecast/OHZ039",
        "county": "https://api.weather.gov/zones/county/OHC157",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/OHZ039"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KCAK",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -81.44343,
          40.91811
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KCAK",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 369.1128
        },
        "stationIdentifier": "KCAK",
        "name": "Akron Canton Regional Airport",
        "timeZone": "America/New_York",
        "provider": "ASOS-HFM",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 266407.51567525
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 60
        },
        "forecast": "https://api.weather.gov/zones/forecast/OHZ021",
        "county": "https://api.weather.gov/zones/county/OHC153",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/OHZ021"
      }
    },
    {
      "id": "https://api.weather.gov/stations/KCRW",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -81.59139,
          38.37944
        ]
      },
      "properties": {
        "@id": "https://api.weather.gov/stations/KCRW",
        "@type": "wx:ObservationStation",
        "elevation": {
          "unitCode": "wmoUnit:m",
          "value": 299.0088
        },
        "stationIdentifier": "KCRW",
        "name": "Charleston, Yeager Airport",
        "timeZone": "America/New_York",
        "provider": "ASOS-HFM",
        "subProvider": "",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 273199.66550174
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 123
        },
        "forecast": "https://api.weather.gov/zones/forecast/WVZ015",
        "county": "https://api.weather.gov/zones/county/WVC039",
        "fireWeatherZone": "https://api.weather.gov/zones/fire/WVZ015"
      }
    }
  ],
  "observationStations": [
    "https://api.weather.gov/stations/KFFO",
    "https://api.weather.gov/stations/KDAY",
    "https://api.weather.gov/stations/KGDK",
    "https://api.weather.gov/stations/KMGY",
    "https://api.weather.gov/stations/KSGH",
    "https://api.weather.gov/stations/KI68",
    "https://api.weather.gov/stations/KILN",
    "https://api.weather.gov/stations/KHAO",
    "https://api.weather.gov/stations/KRID",
    "https://api.weather.gov/stations/KI74",
    "https://api.weather.gov/stations/KVES",
    "https://api.weather.gov/stations/KOXD",
    "https://api.weather.gov/stations/KUYF",
    "https://api.weather.gov/stations/KI23",
    "https://api.weather.gov/stations/KEDJ",
    "https://api.weather.gov/stations/KI67",
    "https://api.weather.gov/stations/KLUK",
    "https://api.weather.gov/stations/KI69",
    "https://api.weather.gov/stations/KAXV",
    "https://api.weather.gov/stations/KMRT",
    "https://api.weather.gov/stations/KCVG",
    "https://api.weather.gov/stations/KTZR",
    "https://api.weather.gov/stations/KOSU",
    "https://api.weather.gov/stations/KI95",
    "https://api.weather.gov/stations/KAOH",
    "https://api.weather.gov/stations/KRZT",
    "https://api.weather.gov/stations/KLCK",
    "https://api.weather.gov/stations/KDLZ",
    "https://api.weather.gov/stations/KMIE",
    "https://api.weather.gov/stations/KCMH",
    "https://api.weather.gov/stations/KAID",
    "https://api.weather.gov/stations/KLHQ",
    "https://api.weather.gov/stations/KMNN",
    "https://api.weather.gov/stations/KGEZ",
    "https://api.weather.gov/stations/KFGX",
    "https://api.weather.gov/stations/KFDY",
    "https://api.weather.gov/stations/KVTA",
    "https://api.weather.gov/stations/KBAK",
    "https://api.weather.gov/stations/KFWA",
    "https://api.weather.gov/stations/KIND",
    "https://api.weather.gov/stations/KEYE",
    "https://api.weather.gov/stations/KMFD",
    "https://api.weather.gov/stations/KFFT",
    "https://api.weather.gov/stations/KLEX",
    "https://api.weather.gov/stations/KZZV",
    "https://api.weather.gov/stations/KHTS",
    "https://api.weather.gov/stations/KLOU",
    "https://api.weather.gov/stations/KSDF",
    "https://api.weather.gov/stations/KBJJ",
    "https://api.weather.gov/stations/KPKB",
    "https://api.weather.gov/stations/KPHD",
    "https://api.weather.gov/stations/KCAK",
    "https://api.weather.gov/stations/KCRW"
  ],
  "pagination": {
    "next": "https://api.weather.gov/stations?id%5B0%5D=KAID&id%5B1%5D=KAOH&id%5B2%5D=KAXV&id%5B3%5D=KBAK&id%5B4%5D=KBJJ&id%5B5%5D=KCAK&id%5B6%5D=KCMH&id%5B7%5D=KCRW&id%5B8%5D=KCVG&id%5B9%5D=KDAY&id%5B10%5D=KDLZ&id%5B11%5D=KEDJ&id%5B12%5D=KEYE&id%5B13%5D=KFDY&id%5B14%5D=KFFO&id%5B15%5D=KFFT&id%5B16%5D=KFGX&id%5B17%5D=KFWA&id%5B18%5D=KGDK&id%5B19%5D=KGEZ&id%5B20%5D=KHAO&id%5B21%5D=KHTS&id%5B22%5D=KI23&id%5B23%5D=KI67&id%5B24%5D=KI68&id%5B25%5D=KI69&id%5B26%5D=KI74&id%5B27%5D=KI95&id%5B28%5D=KILN&id%5B29%5D=KIND&id%5B30%5D=KLCK&id%5B31%5D=KLEX&id%5B32%5D=KLHQ&id%5B33%5D=KLOU&id%5B34%5D=KLUK&id%5B35%5D=KMFD&id%5B36%5D=KMGY&id%5B37%5D=KMIE&id%5B38%5D=KMNN&id%5B39%5D=KMRT&id%5B40%5D=KOSU&id%5B41%5D=KOXD&id%5B42%5D=KPHD&id%5B43%5D=KPKB&id%5B44%5D=KRID&id%5B45%5D=KRZT&id%5B46%5D=KSDF&id%5B47%5D=KSGH&id%5B48%5D=KTZR&id%5B49%5D=KUYF&id%5B50%5D=KVES&id%5B51%5D=KVTA&id%5B52%5D=KZZV&cursor=eyJzIjo1MDB9"
  }
}


"Timestamp": properties.get("timestamp"),
        "Temperature": parse_value(properties.get("temperature"), "°C"),
        "Relative Humidity": parse_value(properties.get("relativeHumidity"), "%"),
        "Barometric Pressure": parse_value(properties.get("barometricPressure"), "Pa"),
        "Wind Speed": parse_value(properties.get("windSpeed"), "km/h"),
        "Rainfall (Last Hour)": parse_value(properties.get("precipitationLastHour"), "m")