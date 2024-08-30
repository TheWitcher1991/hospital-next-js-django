'use client'

import { FC } from 'react'
import { useCheckAuth } from '@/models/account'
import styles from './index.module.css'
import { HeaderMenuList } from '@/widgets/header/HeaderMenu/header-menu-list'
import { guestRoutes } from '@/widgets/header/HeaderMenu/index.utils'

export const HeaderMenu: FC = () => {
	const { isAuthenticated, role } = useCheckAuth()

	return (
		<ul className={styles.header__menu}>
			{!isAuthenticated && <HeaderMenuList menu={guestRoutes} />}
		</ul>
	)
}
