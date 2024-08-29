import { RootState } from '@/store/index.store'

export const AppSelectors = {
	getAccount: (state: RootState) => state.account,
	getServiceType: (state: RootState) => state.serviceType,
	getService: (state: RootState) => state.service,
}
