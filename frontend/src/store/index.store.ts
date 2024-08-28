import { configureStore } from '@reduxjs/toolkit'
import { RootReducer } from '@/store/index.reducers'
import { AuthService } from '@/models/auth'

export const store = () => {
	return configureStore({
		reducer: RootReducer,
		middleware: (getDefaultMiddleware) =>
			getDefaultMiddleware().concat(AuthService.middleware),
	})
}

export type AppStore = ReturnType<typeof store>
export type RootState = ReturnType<AppStore['getState']>
export type AppDispatch = AppStore['dispatch']
