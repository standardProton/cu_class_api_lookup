

const fs = require('fs');

//const depts = ['ACCT', 'APRD', 'ASEN', 'AIRR', 'ANTH', 'APPM', 'ARAB', 'AREN', 'ARCH', 'ARTF', 'ARTH', 'ARTS', 'AHUM', 'ARSC', 'ASIA', 'ASTR', 'ATLS', 'ATOC', 'BAKR', 'BASE', 'BCHM', 'BMEN', 'BADM', 'BCOR', 'BPOL', 'BSLW', 'BUSM', 'CSVC', 'CLDR', 'CWCV', 'CAMW', 'CEES', 'CHEN', 'CHEM', 'CHIN', 'CINE', 'CVEN', 'GREK', 'CLAS', 'COEN', 'CMCI', 'COMM', 'COMR', 'COML', 'CSCI', 'CSCA', 'CSPB', 'CNCR', 'CCOM', 'CMDP', 'CESR', 'DNCE', 'DANE', 'DTSC', 'DTSA', 'DHUM', 'EALC', 'EBIO', 'ECON', 'EDUC', 'EDUA', 'ECEN', 'ECEA', 'ENEN', 'EHON', 'ENLP', 'EMEN', 'EMEA', 'ENES', 'ENGL', 'ESLG', 'EDEN', 'ESBM', 'ENST', 'ENVD', 'EVEN', 'EPOD', 'ENVS', 'ETHN', 'TDXD', 'FARR', 'FRSI', 'FILM', 'FNCE', 'FINN', 'FYXP', 'FYSM', 'FREN', 'GEEN', 'GEOG', 'GEOL', 'GRMN', 'GSLL', 'GRAD', 'GRTE', 'HEBR', 'HIND', 'HIST', 'HONR', 'HUMN', 'HUEN', 'INDO', 'BAIM', 'INFO', 'IPHY', 'IMUS', 'INST', 'IAFS', 'INBU', 'IAWP', 'INVS', 'ITAL', 'JPNS', 'JWST', 'JRNL', 'KREN', 'LAND', 'LGTC', 'LAMS', 'LATN', 'LAWS', 'LEAD', 'LDSP', 'LGBT', 'LIBB', 'LIBR', 'LING', 'MGMT', 'MKTG', 'ENVM', 'MSEN', 'MATH', 'MBAX', 'MBAC', 'MBAE', 'MCEN', 'MDRP', 'MDST', 'MEMS', 'MILR', 'MCDB', 'MSBC', 'MSBX', 'MUSM', 'MUSC', 'MUEL', 'EMUS', 'NAVR', 'NEPL', 'NRSC', 'NCBE', 'NCCS', 'NCEN', 'NCGR', 'NCIE', 'NCEV', 'NCMU', 'NCTM', 'NCTP', 'NCTH', 'NRLN', 'OPIM', 'ORMG', 'ORGN', 'ORGL', 'OREC', 'PACS', 'PMUS', 'PHIL', 'PHYS', 'PLAN', 'PSCI', 'PORT', 'PRLC', 'PSYC', 'QUEC', 'REAL', 'RCPR', 'RLST', 'RUSS', 'REES', 'SNSK', 'SCAN', 'SEWL', 'SOCY', 'SPAN', 'SLHS', 'STAT', 'STDY', 'SUST', 'SSIR', 'SWED', 'CYBR', 'TLEN', 'THDN', 'THTR', 'TMUS', 'TBTN', 'WGST', 'WRTG'];
const depts = ["CSCI", "MATH"]

const skip_words = ["the", "an", "a", "in", "-", "for", "with", "to", "and", "of", "as", "its", "1", "2", "3", "4", "1:", "2:", "3:", "4:"]

async function start(){
    const name_map = {}; //CSCI 1300 -> Starting Computing
    const lookup_map = {}; //Starting -> CSCI 1300, Computing -> CSCI 1300
    const fetch = await import("node-fetch");

    var duration_total = 0;
    for (let i =0; i < depts.length; i++){

        console.log("Loading " + depts[i]);
        await new Promise(resolve => setTimeout(resolve, 1100)); //respect for api usage

        const res1 = await fetch.default("https://classes.colorado.edu/api/?page=fose&route=search&subject=" + depts[i], {
            method: "POST",
            body: '{"other":{"srcdb":"2241"},"criteria":[{"field":"subject","value":"' + depts[i] + '"}]}'
        });
        const res = await res1.json();
        
        const starttime = (new Date()).getTime();
        if (res.results != undefined){
            for (let j = 0; j < res.results.length; j++){
                const cl = res.results[j];
                name_map[cl.code] = cl.title;
                const title_split = cl.title.split(" ");
                for (let k = 0; k < title_split.length; k++){
                    const word = title_split[k].toLowerCase();
                    if (skip_words.includes(word)) continue;

                    if (lookup_map[word] == undefined) lookup_map[word] = [cl.code];
                    else if (!lookup_map[word].includes(cl.code)) lookup_map[word].push(cl.code);
                    
                    //push deptartment name
                    if (lookup_map[depts[i]] == undefined) lookup_map[depts[i]] = [cl.code];
                    else if (!lookup_map[depts[i]].includes(cl.code)) lookup_map[depts[i]].push(cl.code);
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

//convert all keys to lowercase and resave
async function convertLowerCase(){
    fs.readFile(process.cwd() + "/output/lookup_map.json", 'utf-8', (err, data) => {

        const lookup_map = JSON.parse(data);
        const lookup_map2 = {};
        for (const [key, val] of Object.entries(lookup_map)) {
            lookup_map2[key.toLowerCase()] = val;
        }
        fs.writeFile(process.cwd() + "/output/lookup_map.json", JSON.stringify(lookup_map2), (err) => {console.error(err)});
    });
    //console.log(json_text);
}

start();
