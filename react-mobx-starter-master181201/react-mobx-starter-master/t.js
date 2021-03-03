
search = '?page=1&size=3&id=&a&&=abc&id=100=&cit?y=北京'

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

console.log(parse_qs(search))



