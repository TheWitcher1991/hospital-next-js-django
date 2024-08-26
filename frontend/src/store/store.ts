import {configureStore} from "@reduxjs/toolkit";

export const store = configureStore({
    reducer: {

    },
    middleware: getDefaultMiddleware => getDefaultMiddleware().concat()
})

export type TypeRootState = ReturnType<typeof store.getState>
