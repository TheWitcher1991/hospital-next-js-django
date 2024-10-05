import { CSSProperties, FC, PropsWithChildren, ReactNode } from 'react'

interface ChipProps extends PropsWithChildren {
	variant?: 'default' | 'primary' | 'success' | 'warning' | 'danger'
	size?: Size
	startContent?: ReactNode
	endContent?: ReactNode
}

export const Chip: FC<ChipProps> = ({
	variant = 'default',
	children,
	size = 'sm',
	endContent,
	startContent,
}) => {
	const valiantBackground = {
		default: 'var(--color-bg-300)',
		primary: 'var(--color-primary)',
		success: 'var(--color-success)',
		warning: 'var(--color-warning)',
		danger: 'var(--color-danger)',
	}

	const variantColor = {
		default: 'var(--color-fg-600)',
		primary: 'var(--color-fg-white)',
		success: 'var(--color-fg-white)',
		warning: 'var(--color-fg-white)',
		danger: 'var(--color-fg-white)',
	}

	const variantHeight = {
		sm: '22px',
		md: '28px',
		lg: '32px',
	}

	const variantPadding = {
		sm: '0 6px',
		md: '0 10px',
		lg: '0 14px',
	}

	const variantSize = {
		sm: '14px',
		md: '16px',
		lg: '20px',
	}

	const ChipStyle: CSSProperties = {
		display: 'flex',
		alignItems: 'center',
		gap: '6px',
		borderRadius: '50px',
		backgroundColor: valiantBackground[variant],
		color: variantColor[variant],
		fontSize: variantSize[size],
		padding: variantPadding[size],
		height: variantHeight[size],
	}

	return (
		<div style={ChipStyle}>
			{startContent}
			{children}
			{endContent}
		</div>
	)
}
