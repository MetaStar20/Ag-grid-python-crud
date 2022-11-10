import {createStore, applyMiddleware} from 'redux';
import { composeWithDevTools } from "redux-devtools-extension";
import thunk from 'redux-thunk';
import reducer from "../reducer/reducer" ;// import the your reducer
const initialState = {};

const middleware = [thunk];
const store = new createStore(reducer, initialState, applyMiddleware(...middleware));//give your reducer name
export default store;