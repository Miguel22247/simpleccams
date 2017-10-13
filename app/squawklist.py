from random import shuffle

squawklist = [
	'2240',
	'3237',
	'2031',
	'7227',
	'7575',
	'5206',
	'5222',
	'753',
	'3201',
	'270',
	'1174',
	'2277',
	'2223',
	'7261',
	'7641',
	'3536',
	'2037',
	'4744',
	'1475',
	'5203',
	'6317',
	'516',
	'525',
	'5430',
	'4726',
	'565',
	'3515',
	'3243',
	'7305',
	'4463',
	'6307',
	'1424',
	'2255',
	'5230',
	'563',
	'4227',
	'343',
	'2270',
	'2044',
	'7647',
	'7751',
	'3254',
	'3423',
	'222',
	'374',
	'2725',
	'7642',
	'6363',
	'2011',
	'3246',
	'4740',
	'6470',
	'4705',
	'472',
	'7303',
	'7324',
	'3403',
	'2061',
	'4246',
	'7773',
	'2036',
	'1167',
	'1455',
	'313',
	'2262',
	'354',
	'547',
	'2220',
	'1465',
	'2717',
	'2736',
	'211',
	'3450',
	'6217',
	'535',
	'7632',
	'5436',
	'3234',
	'6204',
	'1474',
	'365',
	'7743',
	'1437',
	'4435',
	'3462',
	'4741',
	'4434',
	'2030',
	'7307',
	'4701',
	'4753',
	'7323',
	'2265',
	'372',
	'5211',
	'7537',
	'236',
	'264',
	'2027',
	'314',
	'6475',
	'3411',
	'6314',
	'7633',
	'2227',
	'4775',
	'5224',
	'2005',
	'303',
	'6235',
	'2050',
	'4447',
	'7571',
	'7027',
	'251',
	'3210',
	'3375',
	'501',
	'6372',
	'263',
	'1165',
	'7714',
	'5666',
	'5232',
	'4446',
	'7635',
	'2271',
	'5223',
	'234',
	'5264',
	'4724',
	'4450',
	'2004',
	'7666',
	'6222',
	'215',
	'4437',
	'6343',
	'4771',
	'767',
	'5663',
	'6362',
	'2210',
	'7646',
	'5231',
	'7275',
	'3510',
	'1072',
	'233',
	'3416',
	'7246',
	'5213',
	'7655',
	'6242',
	'3213',
	'7677',
	'2261',
	'5450',
	'6202',
	'7250',
	'3253',
	'6205',
	'6241',
	'326',
	'3422',
	'301',
	'6352',
	'2275',
	'4443',
	'2273',
	'7024',
	'2234',
	'5465',
	'3402',
	'3244',
	'1472',
	'2216',
	'572',
	'3257',
	'6212',
	'3250',
	'576',
	'2212',
	'2207',
	'7644',
	'5675',
	'3465',
	'7713',
	'201',
	'4717',
	'6330',
	'3417',
	'1425',
	'377',
	'3476',
	'7273',
	'2003',
	'341',
	'5423',
	'246',
	'323',
	'5406',
	'7315',
	'4735',
	'4765',
	'5473',
	'7223',
	'6373',
	'265',
	'5426',
	'766',
	'7263',
	'3434',
	'316',
	'3442',
	'2224',
	'7633',
	'6325',
	'553',
	'340',
	'2226',
	'4223',
	'7644',
	'2727',
	'6232',
	'7703',
	'2721',
	'7312',
	'6245',
	'5422',
	'2246',
	'4757',
	'353',
	'5251',
	'1473',
	'5242',
	'3461',
	'1166',
	'7763',
	'5671',
	'2213',
	'216',
	'5441',
	'735',
	'764',
	'3432',
	'6354',
	'364',
	'277',
	'5236',
	'333',
	'6226',
	'5477',
	'3216',
	'7503',
	'6371',
	'7727',
	'3265',
	'4445',
	'2734',
	'5244',
	'253',
	'1171',
	'7577',
	'7762',
	'4444',
	'7641',
	'5241',
	'5665',
	'7225',
	'2267',
	'3527',
	'2060',
	'7202',
	'6367',
	'5204',
	'3517',
	'4243',
	'5234',
	'2047',
	'4244',
	'4236',
	'755',
	'2075',
	'3404',
	'7213',
	'6365',
	'5664',
	'6333',
	'3425',
	'5427',
	'5456',
	'252',
	'4462',
	'2021',
	'5471',
	'1452',
	'6350',
	'533',
	'3205',
	'5253',
	'577',
	'7233',
	'5474',
	'7731',
	'6326',
	'502',
	'7306',
	'243',
	'3374',
	'3460',
	'5476',
	'5660',
	'507',
	'1176',
	'1175',
	'5667',
	'5205',
	'250',
	'7650',
	'4772',
	'2217',
	'223',
	'1450',
	'2726',
	'217',
	'5243',
	'763',
	'4433',
	'7240',
	'4732',
	'2064',
	'7257',
	'214',
	'344',
	'5263',
	'2705',
	'2006',
	'317',
	'2205',
	'1446',
	'4234',
	'7630',
	'7722',
	'237',
	'355',
	'7251',
	'3473',
	'5472',
	'337',
	'6323',
	'3520',
	'4737',
	'6304',
	'3212',
	'6251',
	'3532',
	'6253',
	'332',
	'4703',
	'1423',
	'7253',
	'7205',
	'2720',
	'7712',
	'6244',
	'4217',
	'474',
	'6225',
	'327',
	'3474',
	'7316',
	'1164',
	'2251',
	'7740',
	'6305',
	'7220',
	'7252',
	'6247',
	'6243',
	'6231',
	'6224',
	'7504',
	'5416',
	'3513',
	'7622',
	'4442',
	'257',
	'7243',
	'5412',
	'2732',
	'7020',
	'5216',
	'3466',
	'276',
	'4746',
	'7657',
	'7232',
	'3263',
	'7710',
	'5435',
	'7264',
	'5433',
	'7645',
	'210',
	'6230',
	'7726',
	'5217',
	'342',
	'2703',
	'6334',
	'4455',
	'4464',
	'3202',
	'4770',
	'2706',
	'6471',
	'1476',
	'7321',
	'2276',
	'543',
	'2737',
	'1433',
	'4432',
	'4702',
	'7721',
	'7201',
	'5452',
	'345',
	'751',
	'7733',
	'7730',
	'4720',
	'7320',
	'6361',
	'3373',
	'4766',
	'1444',
	'1416',
	'7230',
	'242',
	'7715',
	'7663',
	'562',
	'473',
	'5254',
	'7274',
	'7326',
	'5420',
	'3475',
	'6347',
	'6301',
	'2714',
	'3427',
	'357',
	'3277',
	'2723',
	'5270',
	'527',
	'4457',
	'352',
	'2046',
	'573',
	'1430',
	'4742',
	'247',
	'5445',
	'7245',
	'6320',
	'6353',
	'5214',
	'7673',
	'4767',
	'5225',
	'206',
	'213',
	'6370',
	'3270',
	'306',
	'5424',
	'375',
	'3370',
	'6306',
	'7304',
	'7637',
	'2254',
	'3204',
	'7574',
	'5252',
	'7265',
	'231',
	'4460',
	'1410',
	'7014',
	'6257',
	'2221',
	'7643',
	'3222',
	'2716',
	'1071',
	'205',
	'4713',
	'7634',
	'7271',
	'6316',
	'567',
	'321',
	'7570',
	'552',
	'1074',
	'4756',
	'4762',
	'7023',
	'6315',
	'360',
	'7231',
	'3217',
	'6221',
	'6313',
	'6246',
	'6206',
	'6237',
	'4240',
	'5442',
	'7742',
	'3446',
	'2702',
	'532',
	'2041',
	'7267',
	'7660',
	'3372',
	'272',
	'7301',
	'232',
	'761',
	'5467',
	'7702',
	'4465',
	'5413',
	'4733',
	'3451',
	'6250',
	'3261',
	'6312',
	'537',
	'6340',
	'7237',
	'367',
	'575',
	'254',
	'4747',
	'7270',
	'304',
	'4743',
	'3223',
	'2066',
	'1461',
	'730',
	'346',
	'1077',
	'1411',
	'322',
	'511',
	'5661',
	'7651',
	'7022',
	'2253',
	'5453',
	'5414',
	'240',
	'2257',
	'1460',
	'5261',
	'5215',
	'2015',
	'7664',
	'7276',
	'7757',
	'7235',
	'750',
	'523',
	'1415',
	'3447',
	'503',
	'5421',
	'5246',
	'2020',
	'4706',
	'347',
	'7744',
	'5265',
	'260',
	'7760',
	'514',
	'4451',
	'3371',
	'571',
	'7707',
	'7716',
	'271',
	'245',
	'574',
	'7266',
	'1431',
	'2054',
	'3215',
	'6223',
	'746',
	'6346',
	'6256',
	'7745',
	'7244',
	'4235',
	'5016',
	'2007',
	'747',
	'363',
	'7652',
	'7704',
	'2025',
	'7711',
	'5417',
	'226',
	'212',
	'5221',
	'4247',
	'2733',
	'506',
	'544',
	'1160',
	'7325',
	'5247',
	'2232',
	'3464',
	'3264',
	'204',
	'7317',
	'4225',
	'3247',
	'4751',
	'1414',
	'4730',
	'2707',
	'3431',
	'3436',
	'7705',
	'3272',
	'3531',
	'7015',
	'5425',
	'2074',
	'2077',
	'4216',
	'3426',
	'6303',
	'743',
	'7277',
	'6357',
	'4755',
	'371',
	'2244',
	'7222',
	'7206',
	'4224',
	'2215',
	'7025',
	'5014',
	'7505',
	'4764',
	'6211',
	'2024',
	'6302',
	'7635',
	'6310',
	'1422',
	'221',
	'1421',
	'1075',
	'566',
	'5670',
	'7576',
	'536',
	'7207',
	'5235',
	'6341',
	'3472',
	'2010',
	'207',
	'7254',
	'1443',
	'731',
	'745',
	'6227',
	'737',
	'4763',
	'505',
	'7761',
	'7650',
	'3203',
	'4215',
	'1435',
	'7623',
	'5673',
	'2263',
	'366',
	'5202',
	'2236',
	'6342',
	'2713',
	'266',
	'7636',
	'4731',
	'2057',
	'7717',
	'7647',
	'6477',
	'4220',
	'752',
	'733',
	'6203',
	'7216',
	'4734',
	'2237',
	'5677',
	'7017',
	'6331',
	'3414',
	'7747',
	'2051',
	'2053',
	'564',
	'7631',
	'6207',
	'2230',
	'7242',
	'2063',
	'3274',
	'305',
	'550',
	'7661',
	'1456',
	'5463',
	'4436',
	'2256',
	'7720',
	'7671',
	'3523',
	'1413',
	'1464',
	'3522',
	'2722',
	'3424',
	'4452',
	'1454',
	'362',
	'2260',
	'6210',
	'3275',
	'7573',
	'203',
	'2245',
	'4774',
	'3235',
	'6474',
	'7626',
	'225',
	'2243',
	'7645',
	'7764',
	'3470',
	'235',
	'3535',
	'2211',
	'4456',
	'6234',
	'5210',
	'275',
	'7723',
	'1441',
	'7211',
	'3463',
	'7736',
	'7734',
	'7620',
	'330',
	'7770',
	'3437',
	'5466',
	'1463',
	'1466',
	'5431',
	'7217',
	'6240',
	'4461',
	'1462',
	'3514',
	'7724',
	'7754',
	'531',
	'3525',
	'2242',
	'320',
	'504',
	'517',
	'7204',
	'7732',
	'740',
	'3512',
	'7311',
	'3267',
	'335',
	'224',
	'4745',
	'1412',
	'2071',
	'256',
	'7627',
	'255',
	'5245',
	'3407',
	'2072',
	'2055',
	'7501',
	'312',
	'6472',
	'1447',
	'4736',
	'3251',
	'2264',
	'1436',
	'2065',
	'4721',
	'4754',
	'4466',
	'6321',
	'7624',
	'3207',
	'5464',
	'7572',
	'5457',
	'7676',
	'3457',
	'334',
	'1163',
	'1471',
	'2014',
	'470',
	'2062',
	'6215',
	'315',
	'7215',
	'5267',
	'6233',
	'3260',
	'476',
	'267',
	'757',
	'3232',
	'7234',
	'557',
	'6377',
	'6337',
	'5262',
	'540',
	'4725',
	'3225',
	'1442',
	'5257',
	'2040',
	'3271',
	'7502',
	'2247',
	'6324',
	'6335',
	'7327',
	'2026',
	'7672',
	'542',
	'3376',
	'6236',
	'6336',
	'7021',
	'1170',
	'325',
	'7226',
	'5260',
	'3252',
	'2043',
	'7771',
	'6374',
	'556',
	'5674',
	'546',
	'5266',
	'1470',
	'4221',
	'1173',
	'4750',
	'5462',
	'3206',
	'2252',
	'3455',
	'3242',
	'370',
	'5233',
	'2231',
	'3241',
	'765',
	'4723',
	'1451',
	'6360',
	'4710',
	'7667',
	'7646',
	'2272',
	'3227',
	'7765',
	'471',
	'1073',
	'7026',
	'7203',
	'4431',
	'7750',
	'2715',
	'4242',
	'6476',
	'3524',
	'3521',
	'1453',
	'6322',
	'7735',
	'7643',
	'4441',
	'5672',
	'5455',
	'6252',
	'7701',
	'7637',
	'5405',
	'4777',
	'2073',
	'5227',
	'3530',
	'7247',
	'7636',
	'5444',
	'2023',
	'4232',
	'350',
	'2214',
	'1477',
	'2266',
	'324',
	'3226',
	'2076',
	'6351',
	'521',
	'7255',
	'3256',
	'7725',
	'273',
	'1432',
	'3211',
	'4245',
	'734',
	'1070',
	'7262',
	'7224',
	'241',
	'530',
	'3245',
	'7272',
	'6375',
	'7634',
	'560',
	'1426',
	'7741',
	'4241',
	'7654',
	'2012',
	'3477',
	'230',
	'5676',
	'4707',
	'3413',
	'2203',
	'261',
	'2701',
	'4752',
	'5440',
	'7737',
	'5015',
	'2204',
	'3220',
	'7625',
	'274',
	'6254',
	'3410',
	'6213',
	'7212',
	'3221',
	'4776',
	'3420',
	'2016',
	'356',
	'522',
	'5475',
	'3456',
	'361',
	'3445',
	'3233',
	'1161',
	'6311',
	'5437',
	'3415',
	'4773',
	'5470',
	'510',
	'2250',
	'551',
	'3534',
	'3405',
	'7642',
	'526',
	'4760',
	'1427',
	'331',
	'3430',
	'4453',
	'302',
	'7302',
	'6327',
	'1434',
	'2710',
	'2033',
	'3266',
	'5407',
	'7662',
	'3406',
	'736',
	'2206',
	'7536',
	'4231',
	'5432',
	'2731',
	'7775',
	'7665',
	'6364',
	'4761',
	'7621',
	'7221',
	'4226',
	'3236',
	'311',
	'7310',
	'1457',
	'3230',
	'3224',
	'2225',
	'7656',
	'2035',
	'7507',
	'3433',
	'2730',
	'3240',
	'4440',
	'2034',
	'7640',
	'741',
	'3471',
	'3533',
	'7774',
	'5212',
	'307',
	'5411',
	'5402',
	'524',
	'2201',
	'351',
	'5403',
	'512',
	'5240',
	'3516',
	'3511',
	'2042',
	'6214',
	'2724',
	'6344',
	'7706',
	'5404',
	'6201',
	'6345',
	'7674',
	'515',
	'2017',
	'3377',
	'6473',
	'2045',
	'760',
	'376',
	'534',
	'2711',
	'7670',
	'3441',
	'2712',
	'6366',
	'3214',
	'5454',
	'2233',
	'262',
	'5226',
	'4454',
	'3435',
	'202',
	'3467',
	'6356',
	'4716',
	'2241',
	'2235',
	'7675',
	'754',
	'7016',
	'4711',
	'1172',
	'4715',
	'4467',
	'2013',
	'742',
	'6355',
	'244',
	'3444',
	'5013',
	'4233',
	'3537',
	'7766',
	'7256',
	'762',
	'4712',
	'5256',
	'7314',
	'336',
	'744',
	'3412',
	'6376',
	'2002',
	'3273',
	'5443',
	'2052',
	'5434',
	'7752',
	'310',
	'554',
	'5461',
	'4470',
	'5446',
	'5250',
	'6216',
	'4727',
	'7753',
	'2056',
	'7260',
	'3454',
	'2735',
	'7756',
	'7653',
	'5410',
	'7313',
	'4714',
	'3255',
	'7214',
	'541',
	'3452',
	'7772',
	'5201',
	'3276',
	'5220',
	'7236',
	'513',
	'5460',
	'6255',
	'7755',
	'3440',
	'5451',
	'3231',
	'227',
	'7210',
	'4704',
	'555',
	'3453',
	'1440',
	'6332',
	'4430',
	'3401',
	'7767',
	'477',
	'1445',
	'3421',
	'2070',
	'4222',
	'2001',
	'2202',
	'545',
	'2704',
	'7506',
	'4237',
	'2032',
	'1417',
	'520',
	'2067',
	'3526',
	'4230',
	'5662',
	'1467',
	'570',
	'2022',
	'220',
	'561',
	'5237',
	'7640',
	'1162',
	'5207',
	'5017',
	'6220',
	'7322',
	'756',
	'1076',
	'5415',
	'1420',
	'4722',
	'5447',
	'373',
	'3262',
	'2222',
	'732',
	'7241',
	'475',
	'5255',
	'3443',
	'7746',
	'5401',
	'2274']

shuffle(squawklist)
