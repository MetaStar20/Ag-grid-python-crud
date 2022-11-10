import {createSelector} from 'reselect';
const gData= state => state;
//const gCount = state => state.data1.count;
const UpdateData = createSelector(
[gData],(data1) => {
    // debugger
        return {currentData: data1.data, isUpdated: data1.isUpdated};
    }
)

export default UpdateData;

