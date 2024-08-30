import { RootReducer } from '@/store/index.reducers'
import { persistReducer } from 'redux-persist'
import storage from 'redux-persist/lib/storage'

const persistConfig = {
	key: 'root',
	storage: storage,
	whitelist: ['account'],
}

export const persistedReducer = persistReducer(persistConfig, RootReducer)
