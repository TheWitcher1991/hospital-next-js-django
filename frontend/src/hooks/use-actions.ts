import {useDispatch} from "react-redux";
import {bindActionCreators} from "redux";
import {NEXT_APP_ACTIONS} from "@/store";

export const useActions = () => {
    const dispatch = useDispatch();

    return bindActionCreators(NEXT_APP_ACTIONS, dispatch)
}
