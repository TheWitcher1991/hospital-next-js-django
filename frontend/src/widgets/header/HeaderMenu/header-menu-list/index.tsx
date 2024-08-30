import { FC } from 'react'
import { HeaderMenuLink } from '@/widgets/header/HeaderMenu/index.types'
import Link from 'next/link'

interface HeaderMenuListProps {
	menu: HeaderMenuLink[]
}

export const HeaderMenuList: FC<HeaderMenuListProps> = ({ menu }) => {
	return menu.map((e, i) => (
		<Link key={i} href={e.to}>
			{e.name}
		</Link>
	))
}
