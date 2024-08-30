import { CSSProperties, FC, PropsWithChildren } from 'react'

interface FlexProps extends PropsWithChildren {
	flexDirection?: CSSProperties['flexDirection']
	flexWrap?: CSSProperties['flexWrap']
	justifyContent?: CSSProperties['justifyContent']
	alignItems?: CSSProperties['alignItems']
	alignContent?: CSSProperties['alignContent']
	flexBasis?: CSSProperties['flexBasis']
	flexGrow?: CSSProperties['flexGrow']
	flex?: CSSProperties['flex']
	flexShrink?: CSSProperties['flexShrink']
	gap?: CSSProperties['gap']
}

export const Flex: FC<FlexProps> = ({
	children,
	flexDirection,
	flexWrap,
	justifyContent,
	alignItems,
	alignContent,
	flexBasis,
	flexGrow,
	flexShrink,
	flex,
	gap,
}) => {
	const style: CSSProperties = {
		display: 'flex',
		flexDirection,
		flexWrap,
		justifyContent,
		alignItems,
		alignContent,
		flexBasis,
		flexGrow,
		flex,
		flexShrink,
		gap,
	}

	return <div style={style}>{children}</div>
}
