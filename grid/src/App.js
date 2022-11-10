import * as React from "react";
import "./App.css";
import {
  ColumnDirective,
  Edit,
  ColumnsDirective,
  Filter,
  GridComponent,
  Inject,
  Page,
  Sort,
  Search,
  Toolbar,
  ColumnChooser,
  Reorder
} from "@syncfusion/ej2-react-grids";
import { InfiniteScroll } from '@syncfusion/ej2-react-grids';

import { connect } from "react-redux";
import UpdateData from "./selector";
import { getData } from "./reducer/action";
import {
  Grid_Paging,
  Grid_Sorting,
  Grid_Filtering,
  Grid_Add,
  Grid_Editing,
  Grid_Delete,
} from "./reducer/action";

class App extends React.Component {
  constructor() {
    super();
    this.gState = {};
  }

  pageSettings = { pageCount: 4, pageSize: 200, enableQueryString: true};
  infiniteOptions = { initialBlocks: 5 };

  validationRule = { required: true };
  orderidRules = { required: true, number: true };
  editOptions = { allowEditing: true, allowAdding: true, allowDeleting: true };
  toolbarOptions = [
    "Search",
    "Add",
    "Edit",
    "Delete",
    "Update",
    "Cancel",
    "ColumnChooser",
  ];
  filterOptions = { type: "Menu" };
  searchOptions = {
    ignoreCase: true,
    operator: "contains",
  };

  dataStateChange(args) {
    // this event will be triggered when peforming any Grid action

    const query = this.gridInstance.getDataModule().generateQuery(true); // get the Grid query without pagination

    // dispatch  the page query
    if (
      args.action.requestType == "paging" ||
      args.action.requestType == "refresh" ||
      args.action.requestType == "delete"
    ) {
      this.props.getData(query, args);
    }
    // dispatch  the filtering query
    if (args.action.requestType == "filtering") {
      this.props.getData(query, args);
    }
    // dispatch  the sorting query
    if (args.action.requestType == "sorting") {
      this.props.getData(query, args);
    }

    // dispatch  the sorting query
    if (args.action.requestType == "searching") {
      this.props.getData(query, args);
    }
  }
  dataSourceChanged(state) {
    // this event will be triggered when we peform CRUD action

    this.gState = Object.assign(this.gState, state); // store the Grid aync process

    const query = this.gridInstance.getDataModule().generateQuery(true); // get the Grid query without pagination

    // dispatch the editing  action
    if (state.action == "edit") {
      this.props.getData(query, state);
    }

    // dispatch the insert action
    else if (state.action == "add") {
      this.props.getData(query, state);
    }

    // dispatch the delete action
    else if (state.requestType == "delete") {
      this.props.getData(query, state);
    } else {
      this.props.getData(query, state);
    }
  }


  componentDidMount() {
    const query = this.gridInstance.getDataModule().generateQuery();
    this.props.getData(query, { skip: 0, take: 200 });
  }

  componentDidUpdate(prevProps, prevState, snapshot) {
    this.gridInstance.hideSpinner();
    if (this.props.data1.isUpdated) {
      this.gState.endEdit(); // To complete Grid CRUD - async process
      // this.gridInstance.freezeRefresh();
    }
  }

  render() {
    // render the EJ2 Grid component
    return (
      <GridComponent
      height={600} 
        ref={(grid) => (this.gridInstance = grid)}
        dataSource={this.props.data1.currentData}
        dataStateChange={this.dataStateChange.bind(this)}
        dataSourceChanged={this.dataSourceChanged.bind(this)}
        searchSettings={this.searchOptions}
        filterSettings={this.filterOptions}
        allowSorting={true}
        editSettings={this.editOptions}
        toolbar={this.toolbarOptions}
        allowFiltering={true}
        showColumnChooser={true}
        allowReordering={true}
        allowPaging={true}
        pageSettings={this.pageSettings}
      >
        <ColumnsDirective>
          <ColumnDirective
            field="X"
            headerText="X"
            width="120"
            textAlign="left"
          ></ColumnDirective>
          <ColumnDirective
            field="Y"
            headerText="Y"
            width="120"
            textAlign="left"
          ></ColumnDirective>
          <ColumnDirective
            field="OBJECTID"
            headerText="OBJECTID"
            width="120"
            textAlign="left"
            isPrimaryKey={true}
          ></ColumnDirective>
          <ColumnDirective
            field="FOLIO"
            headerText="FOLIO"
            width="120"
            textAlign="left"
          ></ColumnDirective>

          <ColumnDirective
            field="TTRRSS"
            headerText="TTRRSS"
            width="120"
            textAlign="left"
          ></ColumnDirective>

          <ColumnDirective
            field="X_COORD"
            headerText="X_COORD"
            width="120"
            textAlign="left"
          ></ColumnDirective>

          <ColumnDirective
            field="Y_COORD"
            headerText="Y_COORD"
            width="120"
            textAlign="left"
          ></ColumnDirective>

          <ColumnDirective
            field="TRUE_SITE_ADDR"
            headerText="TRUE_SITE_ADDR"
            width="120"
            textAlign="left"
          ></ColumnDirective>

          <ColumnDirective
            field="TRUE_SITE_UNIT"
            headerText="TRUE_SITE_UNIT"
            width="120"
            textAlign="left"
          ></ColumnDirective>

          <ColumnDirective
            field="TRUE_SITE_CITY"
            headerText="TRUE_SITE_CITY"
            width="120"
            textAlign="left"
          ></ColumnDirective>

          <ColumnDirective
            field="TRUE_SITE_ZIP_CODE"
            headerText="TRUE_SITE_ZIP_CODE"
            width="120"
            textAlign="left"
          ></ColumnDirective>

          <ColumnDirective
            field="TRUE_MAILING_ADDR1"
            headerText="TRUE_MAILING_ADDR1"
            width="120"
            textAlign="left"
          ></ColumnDirective>

          <ColumnDirective
            field="TRUE_MAILING_ADDR2"
            headerText="TRUE_MAILING_ADDR2"
            width="120"
            textAlign="left"
          ></ColumnDirective>

          <ColumnDirective
            field="TRUE_MAILING_ADDR3"
            headerText="TRUE_MAILING_ADDR3"
            width="120"
            textAlign="left"
          ></ColumnDirective>

          <ColumnDirective
            field="TRUE_MAILING_CITY"
            headerText="TRUE_MAILING_CITY"
            width="120"
            textAlign="left"
          ></ColumnDirective>

          <ColumnDirective
            field="TRUE_MAILING_STATE"
            headerText="TRUE_MAILING_STATE"
            width="120"
            textAlign="left"
          ></ColumnDirective>

          <ColumnDirective
            field="TRUE_MAILING_ZIP_CODE"
            headerText="TRUE_MAILING_ZIP_CODE"
            width="120"
            textAlign="left"
          ></ColumnDirective>

          <ColumnDirective
            field="TRUE_MAILING_COUNTRY"
            headerText="TRUE_MAILING_COUNTRY"
            width="120"
            textAlign="left"
          ></ColumnDirective>

          <ColumnDirective
            field="TRUE_OWNER1"
            headerText="TRUE_OWNER1"
            width="120"
            textAlign="left"
          ></ColumnDirective>

          <ColumnDirective
            field="TRUE_OWNER2"
            headerText="TRUE_OWNER2"
            width="120"
            textAlign="left"
          ></ColumnDirective>

          <ColumnDirective
            field="TRUE_OWNER3"
            headerText="TRUE_OWNER3"
            width="120"
            textAlign="left"
          ></ColumnDirective>

          <ColumnDirective
            field="CONDO_FLAG"
            headerText="CONDO_FLAG"
            width="120"
            textAlign="left"
          ></ColumnDirective>

          <ColumnDirective
            field="PARENT_FOLIO"
            headerText="PARENT_FOLIO"
            width="120"
            textAlign="left"
          ></ColumnDirective>

          <ColumnDirective
            field="DOR_CODE_CUR"
            headerText="DOR_CODE_CUR"
            width="120"
            textAlign="left"
          ></ColumnDirective>

          <ColumnDirective
            field="DOR_DESC"
            headerText="DOR_DESC"
            width="120"
            textAlign="left"
          ></ColumnDirective>

          <ColumnDirective
            field="SUBDIVISION"
            headerText="SUBDIVISION"
            width="120"
            textAlign="left"
          ></ColumnDirective>

          <ColumnDirective
            field="BEDROOM_COUNT"
            headerText="BEDROOM_COUNT"
            width="120"
            textAlign="left"
          ></ColumnDirective>

          <ColumnDirective
            field="BATHROOM_COUNT"
            headerText="BATHROOM_COUNT"
            width="120"
            textAlign="left"
          ></ColumnDirective>

          <ColumnDirective
            field="HALF_BATHROOM_COUNT"
            headerText="HALF_BATHROOM_COUNT"
            width="120"
            textAlign="left"
          ></ColumnDirective>

          <ColumnDirective
            field="FLOOR_COUNT"
            headerText="FLOOR_COUNT"
            width="120"
            textAlign="left"
          ></ColumnDirective>

          <ColumnDirective
            field="UNIT_COUNT"
            headerText="UNIT_COUNT"
            width="120"
            textAlign="left"
          ></ColumnDirective>

          <ColumnDirective
            field="BUILDING_ACTUAL_AREA"
            headerText="BUILDING_ACTUAL_AREA"
            width="120"
            textAlign="left"
          ></ColumnDirective>

          <ColumnDirective
            field="BUILDING_HEATED_AREA"
            headerText="BUILDING_HEATED_AREA"
            width="120"
            textAlign="left"
          ></ColumnDirective>

          <ColumnDirective
            field="LOT_SIZE"
            headerText="LOT_SIZE"
            width="120"
            textAlign="left"
          ></ColumnDirective>

          <ColumnDirective
            field="YEAR_BUILT"
            headerText="YEAR_BUILT"
            width="120"
            textAlign="left"
          ></ColumnDirective>

          <ColumnDirective
            field="ASSESSMENT_YEAR_CUR"
            headerText="ASSESSMENT_YEAR_CUR"
            width="120"
            textAlign="left"
          ></ColumnDirective>

          <ColumnDirective
            field="ASSESSED_VAL_CUR"
            headerText="ASSESSED_VAL_CUR"
            width="120"
            textAlign="left"
          ></ColumnDirective>
          <ColumnDirective
            field="DOS_1"
            headerText="DOS_1"
            width="120"
            textAlign="left"
          ></ColumnDirective>
          <ColumnDirective
            field="PRICE_1"
            headerText="PRICE_1"
            width="120"
            textAlign="left"
          ></ColumnDirective>
          <ColumnDirective
            field="LEGAL"
            headerText="LEGAL"
            width="120"
            textAlign="left"
          ></ColumnDirective>
          <ColumnDirective
            field="PID"
            headerText="PID"
            width="120"
            textAlign="left"
          ></ColumnDirective>
          <ColumnDirective
            field="DATEOFSALE_UTC"
            headerText="DATEOFSALE_UTC"
            width="120"
            textAlign="left"
          ></ColumnDirective>
        </ColumnsDirective>
        <Inject
          services={[
            Page,
            InfiniteScroll,
            Sort,
            Filter,
            Edit,
            Toolbar,
            Search,
            ColumnChooser,
            Reorder
            
          ]}
        />
      </GridComponent>
    );
  }
}
const mapStateToProps = (state, props) => {
  // UpdateData is a reselect selector
  return { data1: UpdateData(state) };
};

// const mapDispatchToProps = dispatch => {
//   return {
//     dispatch
//   }
// }

export default connect(mapStateToProps, { getData })(App);
