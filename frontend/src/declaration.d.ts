declare module '.module.css'

declare global {
	type EmptyObject = Record<string, never>

	type Nullable<T> = T | null

	type LiteralUnion<T extends U, U> = T | (U & Record<any, any>)

	type Size = 'sm' | 'md' | 'lg'

	export interface ListResponse<T> {
		count: number
		pages: number
		next: Nullable<string>
		previous: Nullable<string>
		results: T[] | []
	}

	export interface PaginationOptions {
		page: number
		page_size: number
	}

	interface ChildrenProps {
		children: React.ReactNode
	}

	type OmitClassName<T> = Omit<T, 'className'>

	type DetailedDivProps = React.DetailedHTMLProps<
		React.ButtonHTMLAttributes<HTMLDivElement>,
		HTMLDivElement
	>

	type DetailedButtonProps = React.DetailedHTMLProps<
		React.ButtonHTMLAttributes<HTMLButtonElement>,
		HTMLButtonElement
	>

	type DetailedInputProps = React.DetailedHTMLProps<
		React.InputHTMLAttributes<HTMLInputElement>,
		HTMLInputElement
	>

	type DetailedSelectProps = React.DetailedHTMLProps<
		React.SelectHTMLAttributes<HTMLSelectElement>,
		HTMLSelectElement
	>

	type DetailedLabelProps = React.DetailedHTMLProps<
		React.LabelHTMLAttributes<HTMLLabelElement>,
		HTMLLabelElement
	>

	type DetailedTextareaProps = React.DetailedHTMLProps<
		React.TextareaHTMLAttributes<HTMLTextAreaElement>,
		HTMLTextAreaElement
	>
}
