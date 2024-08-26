declare module '.module.css'

declare global {

    type EmptyObject = Record<string, never>

    type Nullable<T> = T | null

    type LiteralUnion<T extends U, U> = T | (U & Record<any, any>)

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

    type DivProps = React.DetailedHTMLProps<
        React.ButtonHTMLAttributes<HTMLDivElement>,
        HTMLDivElement
    >

    type ButtonProps = React.DetailedHTMLProps<
        React.ButtonHTMLAttributes<HTMLButtonElement>,
        HTMLButtonElement
    >

    type InputProps = React.DetailedHTMLProps<
        React.InputHTMLAttributes<HTMLInputElement>,
        HTMLInputElement
    >

    type SelectProps = React.DetailedHTMLProps<
        React.SelectHTMLAttributes<HTMLSelectElement>,
        HTMLSelectElement
    >

    type LabelProps = React.DetailedHTMLProps<
        React.LabelHTMLAttributes<HTMLLabelElement>,
        HTMLLabelElement
    >

    type TextareaProps = React.DetailedHTMLProps<
        React.TextareaHTMLAttributes<HTMLTextAreaElement>,
        HTMLTextAreaElement
    >

}
