import http from "../serverapi";
import axios from 'axios';

class orderDataService {
  getAll(gState) {
    // debugger
    let cpage = (gState.skip / gState.take);
    let sortColumnName = ''
    let sortDirection = ''

    let params = {};

    params._page = cpage;
    params._limit =  gState.take;


    if (gState.action && gState.action.searchString) {
      params._search = gState.action.searchString
    }

    // push the sorted columns
    if (gState.sorted) {
      for (let i = gState.sorted.length; i > 0; i--) {
        let sortD = gState.sorted[i - 1].direction == "ascending" ? 'asc' : 'desc';
        let sortCol = gState.sorted[i - 1].name;
        sortColumnName = sortColumnName == '' ? sortCol : sortColumnName + ',' + sortCol;
        sortDirection = sortDirection == '' ? sortD : sortDirection + ',' + sortD;
      }
      params._sort = sortColumnName;
      params._order = sortDirection;
    }

    if (gState.where) {
      let filterCol = gState.where[0].predicates;
      for (let i = 0; i < filterCol.length; i++) {
        let optr = filterCol[i].operator == 'contains' ? '_like' : filterCol[i].operator == 'greaterthan' ? '_gte' : filterCol[i].operator == 'lessthan' ? '_lte' : '_equal';
        params[optr] = filterCol[i].field + "__0__" + filterCol[i].value;
      }
    }
    return http.get("/book/",
      {
        params
      });
  }



  getCount() {
    return http.get("/book/count");
  }


  create(data) {
    return http.post("/book/", data);
  }

  update(id, data) {
    return http.put(`/book/${id}`, data);
  }

  remove(id) {
    return http.delete(`/book/${id}`);
  }
}

export default new orderDataService();