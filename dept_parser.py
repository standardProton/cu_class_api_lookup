import re

#inspect element and get full list, remove parent div
#html = """
#<div data-value="">Any Subject</div><div data-value="ACCT">Accounting (ACCT)</div><div data-value="APRD">Advertising, PR, Media Design (APRD)</div><div data-value="ASEN">Aerospace Engineering (ASEN)</div><div data-value="AIRR">Air Force Aerospace Studies (AIRR)</div><div data-value="ANTH">Anthropology (ANTH)</div><div data-value="APPM">Applied Math (APPM)</div><div data-value="ARAB">Arabic (ARAB)</div><div data-value="AREN">Architectural Engineering (AREN)</div><div data-value="ARCH">Architecture (ARCH)</div><div data-value="ARTF">Art Film Studies (ARTF)</div><div data-value="ARTH">Art History (ARTH)</div><div data-value="ARTS">Art Studio and Non-Studio (ARTS)</div><div data-value="AHUM">Arts &amp; Humanities (AHUM)</div><div data-value="ARSC">Arts &amp; Sciences Courses (ARSC)</div><div data-value="ASIA">Asian Studies (ASIA)</div><div data-value="ASTR">Astrophysical &amp; Planetary Sci (ASTR)</div><div data-value="ATLS">ATLAS (ATLS)</div><div data-value="ATOC">Atmospheric &amp; Oceanic Sciences (ATOC)</div><div data-value="BASE">BCOR Applied Semester Exper (BASE)</div><div data-value="BCHM">Biochemistry (BCHM)</div><div data-value="BMEN">Biomedical Engineering (BMEN)</div><div data-value="BADM">Business Administration (BADM)</div><div data-value="BCOR">Business Core (BCOR)</div><div data-value="BSLW">Business Law (BSLW)</div><div data-value="BUSM">Business Minor (BUSM)</div><div data-value="CSVC">Career Services (CSVC)</div><div data-value="CWCV">Center for Western Civilizatio (CWCV)</div><div data-value="CAMW">Center of the American West (CAMW)</div><div data-value="CHEN">Chemical Engineering (CHEN)</div><div data-value="CHEM">Chemistry (CHEM)</div><div data-value="CHIN">Chinese (CHIN)</div><div data-value="CINE">Cinema Stds/Moving Image Arts (CINE)</div><div data-value="CVEN">Civil Engineering (CVEN)</div><div data-value="GREK">Classical Greek Language (GREK)</div><div data-value="CLAS">Classics (CLAS)</div><div data-value="COEN">Coll of Engineerng&amp;App Sci Adm (COEN)</div><div data-value="CMCI">Coll of Media,Commncation,Info (CMCI)</div><div data-value="COMM">Communication (COMM)</div><div data-value="COML">Comparative Literature (COML)</div><div data-value="CSCI">Computer Science (CSCI)</div><div data-value="CSPB">Computer Science Post Bacc (CSPB)</div><div data-value="CCOM">Corporate Communication (CCOM)</div><div data-value="CMDP">Critical Media Practices (CMDP)</div><div data-value="CESR">Curr Emphasis in Soc Respnsbly (CESR)</div><div data-value="DNCE">Dance (DNCE)</div><div data-value="DTSC">Data Science (DTSC)</div><div data-value="DHUM">Digital Humanities (DHUM)</div><div data-value="EBIO">Ecology &amp; Evolutionary Biology (EBIO)</div><div data-value="ECON">Economics (ECON)</div><div data-value="EDUC">Education (EDUC)</div><div data-value="ECEN">Electrical &amp; Computer Engr (ECEN)</div><div data-value="EHON">Engineering Honors (EHON)</div><div data-value="ENLP">Engineering Leadership Program (ENLP)</div><div data-value="EMEN">Engineering Management (EMEN)</div><div data-value="ENES">Engineering, Ethics &amp; Society (ENES)</div><div data-value="ENGL">English (ENGL)</div><div data-value="ESLG">English as a Second Language (ESLG)</div><div data-value="ESBM">Entrepren &amp; Small Bus Mgmt (ESBM)</div><div data-value="ENVD">Environmental Design (ENVD)</div><div data-value="EVEN">Environmental Engineering (EVEN)</div><div data-value="EPOD">Environmental Prod of Design (EPOD)</div><div data-value="ENVS">Environmental Studies (ENVS)</div><div data-value="ETHN">Ethnic Studies (ETHN)</div><div data-value="FNCE">Finance (FNCE)</div><div data-value="FYXP">First Year Exploration (FYXP)</div><div data-value="FREN">French (FREN)</div><div data-value="GEEN">General Engineering (GEEN)</div><div data-value="GEOG">Geography (GEOG)</div><div data-value="GEOL">Geological Sciences (GEOL)</div><div data-value="GRMN">German (GRMN)</div><div data-value="GSLL">Germanic &amp; Slavic Lang &amp; Lit (GSLL)</div><div data-value="GRAD">Graduate School (GRAD)</div><div data-value="HEBR">Hebrew (HEBR)</div><div data-value="HIND">Hindi/Urdu (HIND)</div><div data-value="HIST">History (HIST)</div><div data-value="HONR">Honors (HONR)</div><div data-value="HUMN">Humanities (HUMN)</div><div data-value="INDO">Indonesian (INDO)</div><div data-value="BAIM">Infm Mgmt/Business Analytics (BAIM)</div><div data-value="INFO">Information Science (INFO)</div><div data-value="IPHY">Integrative Physiology (IPHY)</div><div data-value="IAFS">International Affairs (IAFS)</div><div data-value="INBU">International Business Cert (INBU)</div><div data-value="IAWP">Intrmedia Art,Wrtg,Performance (IAWP)</div><div data-value="INVS">INVST Community Studies (INVS)</div><div data-value="ITAL">Italian (ITAL)</div><div data-value="JPNS">Japanese (JPNS)</div><div data-value="JWST">Jewish Studies (JWST)</div><div data-value="JRNL">Journalism (JRNL)</div><div data-value="KREN">Korean (KREN)</div><div data-value="LAND">Landscape Architecture (LAND)</div><div data-value="LAMS">Latin American Studies (LAMS)</div><div data-value="LATN">Latin Language (LATN)</div><div data-value="LAWS">Law School (LAWS)</div><div data-value="LEAD">Leadership (LEAD)</div><div data-value="LGBT">Lesbn/Gay/Bisexual Stdys (LGBT)</div><div data-value="LING">Linguistics (LING)</div><div data-value="MGMT">Management (MGMT)</div><div data-value="MKTG">Marketing (MKTG)</div><div data-value="ENVM">Master of the Environment (ENVM)</div><div data-value="MSEN">Materials Science&amp;Engineering (MSEN)</div><div data-value="MATH">Mathematics (MATH)</div><div data-value="MBAX">MBA Advanced Electives (MBAX)</div><div data-value="MBAC">MBA Core (MBAC)</div><div data-value="MCEN">Mechanical Engineering (MCEN)</div><div data-value="MDST">Media Studies (MDST)</div><div data-value="MILR">Military Science (MILR)</div><div data-value="MCDB">Molecular Cell &amp; Dev Biology (MCDB)</div><div data-value="MSBC">MS Business Core (MSBC)</div><div data-value="MSBX">MS Business Electives (MSBX)</div><div data-value="MUSM">Museum (MUSM)</div><div data-value="MUSC">Music (MUSC)</div><div data-value="MUEL">Music Electives (MUEL)</div><div data-value="EMUS">Music Ensemble (EMUS)</div><div data-value="NAVR">Naval Science (NAVR)</div><div data-value="NRSC">Neuroscience (NRSC)</div><div data-value="NRLN">Norlin Scholars (NRLN)</div><div data-value="OPIM">Operations &amp; Information MGMT (OPIM)</div><div data-value="ORMG">Organization Management (ORMG)</div><div data-value="ORGN">Organizational Behavior (ORGN)</div><div data-value="OREC">Outdoor Recreation Economy (OREC)</div><div data-value="PACS">Peace &amp; Conflict Studies (PACS)</div><div data-value="PMUS">Performance Music (PMUS)</div><div data-value="PHIL">Philosophy (PHIL)</div><div data-value="PHYS">Physics (PHYS)</div><div data-value="PLAN">Planning and Urban Design (PLAN)</div><div data-value="PSCI">Political Science (PSCI)</div><div data-value="PORT">Portuguese (PORT)</div><div data-value="PRLC">Presidents Leadership Class (PRLC)</div><div data-value="PSYC">Psychology (PSYC)</div><div data-value="QUEC">Quechua Language Courses (QUEC)</div><div data-value="REAL">Real Estate (REAL)</div><div data-value="RLST">Religious Studies (RLST)</div><div data-value="RUSS">Russian (RUSS)</div><div data-value="REES">Russian/Eastern European Stds (REES)</div><div data-value="SCAN">Scandinavian (SCAN)</div><div data-value="SOCY">Sociology (SOCY)</div><div data-value="SPAN">Spanish (SPAN)</div><div data-value="SLHS">Speech, Language &amp; Hearing Sci (SLHS)</div><div data-value="STAT">Statistics (STAT)</div><div data-value="SWED">Swedish (SWED)</div><div data-value="CYBR">Technology, Cybersec &amp; Policy (CYBR)</div><div data-value="THDN">Theater &amp; Dance (THDN)</div><div data-value="THTR">Theatre (THTR)</div><div data-value="TMUS">Thesis Music (TMUS)</div><div data-value="TBTN">Tibetan (TBTN)</div><div data-value="WGST">Women and Gender Studies (WGST)</div><div data-value="WRTG" class="selected">Writing and Rhetoric (WRTG)</div>
#"""
html = """
<option value="ACCT">Accounting (ACCT)</option>
	<option value="APRD">Advertising, PR, Media Design (APRD)</option>
	<option value="ASEN">Aerospace Engineering (ASEN)</option>
	<option value="AIRR">Air Force Aerospace Studies (AIRR)</option>
	<option value="ANTH">Anthropology (ANTH)</option>
	<option value="APPM">Applied Math (APPM)</option>
	<option value="ARAB">Arabic (ARAB)</option>
	<option value="AREN">Architectural Engineering (AREN)</option>
	<option value="ARCH">Architecture (ARCH)</option>
	<option value="ARTF">Art Film Studies (ARTF)</option>
	<option value="ARTH">Art History (ARTH)</option>
	<option value="ARTS">Art Studio and Non-Studio (ARTS)</option>
	<option value="AHUM">Arts &amp; Humanities (AHUM)</option>
	<option value="ARSC">Arts &amp; Sciences Courses (ARSC)</option>
	<option value="ASIA">Asian Studies (ASIA)</option>
	<option value="ASTR">Astrophysical &amp; Planetary Sci (ASTR)</option>
	<option value="ATLS">ATLAS (ATLS)</option>
	<option value="ATOC">Atmospheric &amp; Oceanic Sciences (ATOC)</option>
	<option value="BAKR" hidden="">Baker Residential Acad Prgm (BAKR)</option>
	<option value="BASE">BCOR Applied Semester Exper (BASE)</option>
	<option value="BCHM">Biochemistry (BCHM)</option>
	<option value="BMEN">Biomedical Engineering (BMEN)</option>
	<option value="BADM">Business Administration (BADM)</option>
	<option value="BCOR">Business Core (BCOR)</option>
	<option value="BPOL">Business Environment &amp; Policy (BPOL)</option>
	<option value="BSLW">Business Law (BSLW)</option>
	<option value="BUSM">Business Minor (BUSM)</option>
	<option value="CSVC">Career Services (CSVC)</option>
	<option value="CLDR" hidden="">Center for Leadership (CLDR)</option>
	<option value="CWCV">Center for Western Civilizatio (CWCV)</option>
	<option value="CAMW">Center of the American West (CAMW)</option>
	<option value="CEES" hidden="">Central &amp; East European Stdy (CEES)</option>
	<option value="CHEN">Chemical Engineering (CHEN)</option>
	<option value="CHEM">Chemistry (CHEM)</option>
	<option value="CHIN">Chinese (CHIN)</option>
	<option value="CINE">Cinema Stds/Moving Image Arts (CINE)</option>
	<option value="CVEN">Civil Engineering (CVEN)</option>
	<option value="GREK">Classical Greek Language (GREK)</option>
	<option value="CLAS">Classics (CLAS)</option>
	<option value="COEN">Coll of Engineerng&amp;App Sci Adm (COEN)</option>
	<option value="CMCI">Coll of Media,Commncation,Info (CMCI)</option>
	<option value="COMM">Communication (COMM)</option>
	<option value="COMR" hidden="">Communication Res Acad Prgm (COMR)</option>
	<option value="COML">Comparative Literature (COML)</option>
	<option value="CSCI">Computer Science (CSCI)</option>
	<option value="CSCA" hidden="">Computer Science (CSCA)</option>
	<option value="CSPB">Computer Science Post Bacc (CSPB)</option>
	<option value="CNCR" hidden="">Concurrent Placeholder (CNCR)</option>
	<option value="CCOM">Corporate Communication (CCOM)</option>
	<option value="CMDP">Critical Media Practices (CMDP)</option>
	<option value="CESR">Curr Emphasis in Soc Respnsbly (CESR)</option>
	<option value="DNCE">Dance (DNCE)</option>
	<option value="DANE" hidden="">Danish (DANE)</option>
	<option value="DTSC">Data Science (DTSC)</option>
	<option value="DTSA" hidden="">Data Science (DTSA)</option>
	<option value="DHUM" hidden="">Digital Humanities (DHUM)</option>
	<option value="EALC" hidden="">East Asian Langs &amp; Civilzatns (EALC)</option>
	<option value="EBIO">Ecology &amp; Evolutionary Biology (EBIO)</option>
	<option value="ECON">Economics (ECON)</option>
	<option value="EDUC">Education (EDUC)</option>
	<option value="EDUA" hidden="">Education (EDUA)</option>
	<option value="ECEN">Electrical &amp; Computer Engr (ECEN)</option>
	<option value="ECEA" hidden="">Electrical &amp; Computer Engr (ECEA)</option>
	<option value="ENEN">Energy Engineering (ENEN)</option>
	<option value="EHON" hidden="">Engineering Honors (EHON)</option>
	<option value="ENLP">Engineering Leadership Program (ENLP)</option>
	<option value="EMEN">Engineering Management (EMEN)</option>
	<option value="EMEA" hidden="">Engineering Management (EMEA)</option>
	<option value="ENES">Engineering, Ethics &amp; Society (ENES)</option>
	<option value="ENGL">English (ENGL)</option>
	<option value="ESLG" hidden="">English as a Second Language (ESLG)</option>
	<option value="EDEN" hidden="">Engr for Developng Communities (EDEN)</option>
	<option value="ESBM">Entrepren &amp; Small Bus Mgmt (ESBM)</option>
	<option value="ENST" hidden="">Environment and Sustainability (ENST)</option>
	<option value="ENVD">Environmental Design (ENVD)</option>
	<option value="EVEN">Environmental Engineering (EVEN)</option>
	<option value="EPOD">Environmental Prod of Design (EPOD)</option>
	<option value="ENVS">Environmental Studies (ENVS)</option>
	<option value="ETHN">Ethnic Studies (ETHN)</option>
	<option value="TDXD" hidden="">Experience Design (TDXD)</option>
	<option value="FARR">Farrand Residential Acad Prgm (FARR)</option>
	<option value="FRSI" hidden="">Farsi (FRSI)</option>
	<option value="FILM" hidden="">Film Studies (FILM)</option>
	<option value="FNCE">Finance (FNCE)</option>
	<option value="FINN" hidden="">Finnish (FINN)</option>
	<option value="FYXP">First Year Exploration (FYXP)</option>
	<option value="FYSM" hidden="">First Year Seminar (FYSM)</option>
	<option value="FREN">French (FREN)</option>
	<option value="GEEN">General Engineering (GEEN)</option>
	<option value="GEOG">Geography (GEOG)</option>
	<option value="GEOL">Geological Sciences (GEOL)</option>
	<option value="GRMN">German (GRMN)</option>
	<option value="GSLL">Germanic &amp; Slavic Lang &amp; Lit (GSLL)</option>
	<option value="GRAD" hidden="">Graduate School (GRAD)</option>
	<option value="GRTE" hidden="">Graduate Teacher Education (GRTE)</option>
	<option value="HEBR">Hebrew (HEBR)</option>
	<option value="HIND">Hindi/Urdu (HIND)</option>
	<option value="HIST">History (HIST)</option>
	<option value="HONR">Honors (HONR)</option>
	<option value="HUMN">Humanities (HUMN)</option>
	<option value="HUEN" hidden="">Humanities for Engineers (HUEN)</option>
	<option value="INDO">Indonesian (INDO)</option>
	<option value="BAIM">Infm Mgmt/Business Analytics (BAIM)</option>
	<option value="INFO">Information Science (INFO)</option>
	<option value="IPHY">Integrative Physiology (IPHY)</option>
	<option value="IMUS" hidden="">Intensive Music (IMUS)</option>
	<option value="INST" hidden="">Interdisciplinary Studies (INST)</option>
	<option value="IAFS">International Affairs (IAFS)</option>
	<option value="INBU">International Business Cert (INBU)</option>
	<option value="IAWP" hidden="">Intrmedia Art,Wrtg,Performance (IAWP)</option>
	<option value="INVS">INVST Community Studies (INVS)</option>
	<option value="ITAL">Italian (ITAL)</option>
	<option value="JPNS">Japanese (JPNS)</option>
	<option value="JWST">Jewish Studies (JWST)</option>
	<option value="JRNL">Journalism (JRNL)</option>
	<option value="KREN">Korean (KREN)</option>
	<option value="LAND">Landscape Architecture (LAND)</option>
	<option value="LGTC" hidden="">Language Technology (LGTC)</option>
	<option value="LAMS">Latin American Studies (LAMS)</option>
	<option value="LATN">Latin Language (LATN)</option>
	<option value="LAWS">Law School (LAWS)</option>
	<option value="LEAD">Leadership (LEAD)</option>
	<option value="LDSP" hidden="">Leadership Res Acad Prgrm (LDSP)</option>
	<option value="LGBT">Lesbn/Gay/Bisexual Stdys (LGBT)</option>
	<option value="LIBB">Libby Residential Acad Prgm (LIBB)</option>
	<option value="LIBR" hidden="">Libraries (LIBR)</option>
	<option value="LING">Linguistics (LING)</option>
	<option value="MGMT">Management (MGMT)</option>
	<option value="MKTG">Marketing (MKTG)</option>
	<option value="ENVM">Master of the Environment (ENVM)</option>
	<option value="MSEN">Materials Science&amp;Engineering (MSEN)</option>
	<option value="MATH">Mathematics (MATH)</option>
	<option value="MBAX">MBA Advanced Electives (MBAX)</option>
	<option value="MBAC">MBA Core (MBAC)</option>
	<option value="MBAE" hidden="">MBA Executive (MBAE)</option>
	<option value="MCEN">Mechanical Engineering (MCEN)</option>
	<option value="MDRP" hidden="">Media Research and Practice (MDRP)</option>
	<option value="MDST">Media Studies (MDST)</option>
	<option value="MEMS" hidden="">Medieval &amp; Early Modern Stdys (MEMS)</option>
	<option value="MILR">Military Science (MILR)</option>
	<option value="MCDB">Molecular Cell &amp; Dev Biology (MCDB)</option>
	<option value="MSBC">MS Business Core (MSBC)</option>
	<option value="MSBX">MS Business Electives (MSBX)</option>
	<option value="MUSM">Museum (MUSM)</option>
	<option value="MUSC">Music (MUSC)</option>
	<option value="MUEL">Music Electives (MUEL)</option>
	<option value="EMUS">Music Ensemble (EMUS)</option>
	<option value="NAVR">Naval Science (NAVR)</option>
	<option value="NEPL" hidden="">Nepali Language and Culture (NEPL)</option>
	<option value="NRSC">Neuroscience (NRSC)</option>
	<option value="NCBE" hidden="">Non-credit Business Education (NCBE)</option>
	<option value="NCCS" hidden="">Non-credit CyberSecurity (NCCS)</option>
	<option value="NCEN" hidden="">Non-credit Engineering (NCEN)</option>
	<option value="NCGR" hidden="">Non-credit German (NCGR)</option>
	<option value="NCIE" hidden="">Non-credit Internat'l English (NCIE)</option>
	<option value="NCEV" hidden="">Non-credit Masters of Environm (NCEV)</option>
	<option value="NCMU" hidden="">Non-credit Music (NCMU)</option>
	<option value="NCTM" hidden="">Non-credit Technology &amp; Media (NCTM)</option>
	<option value="NCTP" hidden="">Non-credit Test Preparation (NCTP)</option>
	<option value="NCTH" hidden="">Non-credit Theater (NCTH)</option>
	<option value="NRLN">Norlin Scholars (NRLN)</option>
	<option value="OPIM">Operations &amp; Information MGMT (OPIM)</option>
	<option value="ORMG">Organization Management (ORMG)</option>
	<option value="ORGN">Organizational Behavior (ORGN)</option>
	<option value="ORGL" hidden="">Organizational Leadership (ORGL)</option>
	<option value="OREC">Outdoor Recreation Economy (OREC)</option>
	<option value="PACS">Peace &amp; Conflict Studies (PACS)</option>
	<option value="PMUS">Performance Music (PMUS)</option>
	<option value="PHIL">Philosophy (PHIL)</option>
	<option value="PHYS">Physics (PHYS)</option>
	<option value="PLAN">Planning and Urban Design (PLAN)</option>
	<option value="PSCI">Political Science (PSCI)</option>
	<option value="PORT">Portuguese (PORT)</option>
	<option value="PRLC">Presidents Leadership Class (PRLC)</option>
	<option value="PSYC">Psychology (PSYC)</option>
	<option value="QUEC">Quechua Language Courses (QUEC)</option>
	<option value="REAL">Real Estate (REAL)</option>
	<option value="RCPR" hidden="">Reciprocal Exchange (RCPR)</option>
	<option value="RLST">Religious Studies (RLST)</option>
	<option value="RUSS">Russian (RUSS)</option>
	<option value="REES">Russian/Eastern European Stds (REES)</option>
	<option value="SNSK" hidden="">Sanskrit (SNSK)</option>
	<option value="SCAN">Scandinavian (SCAN)</option>
	<option value="SEWL" hidden="">Sewall Residential Acad Prgm (SEWL)</option>
	<option value="SOCY">Sociology (SOCY)</option>
	<option value="SPAN">Spanish (SPAN)</option>
	<option value="SLHS">Speech, Language &amp; Hearing Sci (SLHS)</option>
	<option value="STAT">Statistics (STAT)</option>
	<option value="STDY" hidden="">Study Abroad (STDY)</option>
	<option value="SUST" hidden="">Sustainability by Design RAP (SUST)</option>
	<option value="SSIR" hidden="">Sustainablty&amp;Soc Innovtn  RAP (SSIR)</option>
	<option value="SWED">Swedish (SWED)</option>
	<option value="CYBR">Technology, Cybersec &amp; Policy (CYBR)</option>
	<option value="TLEN" hidden="">Telecommunications (TLEN)</option>
	<option value="THDN" hidden="">Theater &amp; Dance (THDN)</option>
	<option value="THTR">Theatre (THTR)</option>
	<option value="TMUS">Thesis Music (TMUS)</option>
	<option value="TBTN">Tibetan (TBTN)</option>
	<option value="WGST">Women and Gender Studies (WGST)</option>
	<option value="WRTG">Writing and Rhetoric (WRTG)</option>
"""


res = re.findall("value=\"....\"", html)

depts = []

for dept_val in res:
    dept = dept_val.replace("value=\"", "")[0:4] #data-value
    depts.append(dept)

print("Found %s departments:\n" % len(depts))
print(depts)