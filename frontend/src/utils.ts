
export function getQueryParams(): { [key: string]: string } {
  return location.search
    ? location.search.substr(1).split("&")
      .reduce((qd, item) => {
        let [k,v] = item.split("=");
        v = v && decodeURIComponent(v);
        (qd[k] = qd[k] || []).push(v);
        return qd;
      }, {})
    : {}
}