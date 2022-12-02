import { orderDetails } from '../data';
import { DataManager, Query } from '@syncfusion/ej2-data';
import {
    Grid_Paging, Grid_Sorting, Grid_Filtering,
    Grid_Add, Grid_Editing, Grid_Delete, Grid_Search
} from './action';

// initially the Grid dataStateChange event is not triggered. here we set default pageSize as take . 
//you can set pageSize based on your application. 
const initialPage = { skip: 0, take: 12 } 
const initialState = {
    data: [],
    error: false,
    result: [],
    count: 0,
    isUpdated: false
}

const reducer = (state = initialState, action, gquery) => {
    
    switch (action.type) {
        case Grid_Paging: {
            return ({
                data: { result: action.payload, count: action.tCount }, isUpdated: false
            })
        }
        case Grid_Filtering: {
            return ({
                data: { result: action.payload, count: action.tCount }, isUpdated: false
            })
        }
        case Grid_Sorting: {
            return ({
                data: { result: action.payload, count: action.tCount }, isUpdated: false
            })
        }
        case Grid_Search: {
            return ({
                data: { result: action.payload, count: action.tCount }, isUpdated: false
            })
        }
        case Grid_Add: {
            
            return ({
                data: { result: action.payload, count: action.tCount }, isUpdated: true,
            })
        }
        case Grid_Editing: {
            
           
            return ({
                data: { result: action.payload, count: action.tCount }, isUpdated: true,
            })
        }
        case Grid_Delete: {
            
            return ({
                data: { result: action.payload, count: action.tCount }, isUpdated: true,
            })
        }
        default: {
            // we need to return the Grid data as result and count with object type
            // const count1 = state.data.length;
            // const data1 = { data: { result: state.data.slice(initialPage.skip, initialPage.take), count: count1 }, isUpdated: false }
             
            return ({data:{result: [], count:0}})
        }
    }
}

export default reducer;
