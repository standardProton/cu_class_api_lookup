

const fs = require('fs');

//const depts = ['ACCT', 'APRD', 'ASEN', 'AIRR', 'ANTH', 'APPM', 'ARAB', 'AREN', 'ARCH', 'ARTF', 'ARTH', 'ARTS', 'AHUM', 'ARSC', 'ASIA', 'ASTR', 'ATLS', 'ATOC', 'BASE', 'BCHM', 'BMEN', 'BADM', 'BCOR', 'BSLW', 'BUSM', 'CSVC', 'CWCV', 'CAMW', 'CHEN', 'CHEM', 'CHIN', 'CINE', 'CVEN', 'GREK', 'CLAS', 'COEN', 'CMCI', 'COMM', 'COML', 'CSCI', 'CSPB', 'CCOM', 'CMDP', 'CESR', 'DNCE', 'DTSC', 'DHUM', 'EBIO', 'ECON', 'EDUC', 'ECEN', 'EHON', 'ENLP', 'EMEN', 'ENES', 'ENGL', 'ESLG', 'ESBM', 'ENVD', 'EVEN', 'EPOD', 'ENVS', 'ETHN', 'FNCE', 'FYXP', 'FREN', 'GEEN', 'GEOG', 'GEOL', 'GRMN', 'GSLL', 'GRAD', 'HEBR', 'HIND', 'HIST', 'HONR', 'HUMN', 'INDO', 'BAIM', 'INFO', 'IPHY', 'IAFS', 'INBU', 'IAWP', 'INVS', 'ITAL', 'JPNS', 'JWST', 'JRNL', 'KREN', 'LAND', 'LAMS', 'LATN', 'LAWS', 'LEAD', 'LGBT', 'LING', 'MGMT', 'MKTG', 'ENVM', 'MSEN', 'MATH', 'MBAX', 'MBAC', 'MCEN', 'MDST', 'MILR', 'MCDB', 'MSBC', 'MSBX', 'MUSM', 'MUSC', 'MUEL', 'EMUS', 'NAVR', 'NRSC', 'NRLN', 'OPIM', 'ORMG', 'ORGN', 'OREC', 'PACS', 'PMUS', 'PHIL', 'PHYS', 'PLAN', 'PSCI', 'PORT', 'PRLC', 'PSYC', 'QUEC', 'REAL', 'RLST', 'RUSS', 'REES', 'SCAN', 'SOCY', 'SPAN', 'SLHS', 'STAT', 'SWED', 'CYBR', 'THDN', 'THTR', 'TMUS', 'TBTN', 'WGST', 'WRTG']
const depts = ["CSCI", "MATH"]

const skip_words = ["the", "an", "a", "in", "-", "for", "with", "to", "and", "of", "as", "its", "1", "2", "3", "4", "1:", "2:", "3:", "4:"]

async function start(){
    const name_map = {}; //CSCI 1300 -> Starting Computing
    const lookup_map = {}; //Starting -> CSCI 1300, Computing -> CSCI 1300
    const fetch = await import("node-fetch");

    var duration_total = 0;
    for (let i =0; i < depts.length; i++){

        console.log("Loading " + depts[i]);
        await new Promise(resolve => setTimeout(resolve, 1000)); //respect for api usage

        const res1 = await fetch.default("https://classes.colorado.edu/api/?page=fose&route=search&subject=" + depts[i], {
            method: "POST",
            body: '{"other":{"srcdb":"2237"},"criteria":[{"field":"subject","value":"' + depts[i] + '"}]}'
        });
        const res = await res1.json();
        
        const starttime = (new Date()).getTime();
        if (res.results != undefined){
            for (let j = 0; j < res.results.length; j++){
                const cl = res.results[j];
                name_map[cl.code] = cl.title;
                const title_split = cl.title.split(" ");
                for (let k = 0; k < title_split.length; k++){
                    const word = title_split[k];
                    if (skip_words.includes(word.toLowerCase())) continue;
                    if (lookup_map[word] == undefined) lookup_map[word] = [cl.code];
                    else if (!lookup_map[word].includes(cl.code)) lookup_map[word].push(cl.code);
                }
            }
        } else {
            console.error("Could not fetch classes for " + depts[i] + ":");
            console.log(res);
        }
        duration_total += (new Date()).getTime() - starttime;
    }

    fs.writeFile(process.cwd() + "/output/name_map.json", JSON.stringify(name_map), (err) => {console.error(err)});
    fs.writeFile(process.cwd() + "/output/lookup_map.json", JSON.stringify(lookup_map), (err) => {console.error(err)});

    console.log("Name map:");
    console.log(name_map);
    console.log("Lookup map:");
    console.log(lookup_map);
    console.log("Took " + duration_total + "ms to process");
}

start();
