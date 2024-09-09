import { FC } from 'react'
import { HeaderButtons } from '@/widgets/header/header-buttons'
import { HeaderMenu } from '@/widgets/header/header-menu'
import { Container, Logo } from '@/shared/ui'
import styles from './header.module.css'

export const Header: FC = () => {
	return (
		<header className={styles.header}>
			<Container>
				<nav className={styles.header__nav}>
					<Logo />
					<HeaderMenu />
					<HeaderButtons />
				</nav>
			</Container>
		</header>
	)
}
