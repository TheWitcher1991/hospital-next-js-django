import { HeaderMenuLink } from '@/widgets/header/HeaderMenu/index.types'

export const guestRoutes: HeaderMenuLink[] = [
	{ to: '/', name: 'Главная' },
	{ to: '/login', name: 'Талоны' },
	{ to: '/login', name: 'Медкарта' },
	{ to: '/about', name: 'О нас' },
	{ to: '/directory', name: 'Справочник' },
]

export const patientRoutes: HeaderMenuLink[] = [
	{ to: '/i', name: 'Дашборд' },
	{ to: '/i/service', name: 'Услуги' },
	{ to: '/i/talon', name: 'Талоны' },
	{ to: '/i/pay', name: 'Платежи' },
	{ to: '/i/medcard', name: 'Медкарта' },
	{ to: '/directory', name: 'Справочник' },
]

export const employeeRoutes: HeaderMenuLink[] = [
	{ to: '/i', name: 'Дашборд' },
	{ to: '/directory', name: 'Справочник' },
]
