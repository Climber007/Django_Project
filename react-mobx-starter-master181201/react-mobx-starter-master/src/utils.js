import React from "react";

const inject = obj => Comp => props => <Comp {...obj} {...props} />;

function parse_qs(qs, re=/([^=?]+)=([^&?]+)/) {
    let obj = {}
    // if (qs.startsWith('?'))
    //     qs = qs.substr(1);
    qs.split('&').forEach(element => {
        match = re.exec(element);
        if (match)
            obj[match[1]] = match[2] // k:[v1,v2] push
    });
    return obj;
}


export {inject, parse_qs};
