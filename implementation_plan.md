# Mobile Responsiveness Overhaul Plan

The goal of this task is to ensure that the entire PXP website ecosystem is fully mobile-friendly and responsive.

## Proposed Changes

### assessment-portal.html
- Line 335: Found fixed large width. Needs `w-full md:w-[...]`.
- Line 335: Found fixed large height. Needs `h-auto md:h-[...]`.
- Line 336: Found fixed large width. Needs `w-full md:w-[...]`.
- Line 336: Found fixed large height. Needs `h-auto md:h-[...]`.
- Line 541: Found fixed large width. Needs `w-full md:w-[...]`.

### corporate-email.html
- Line 336: Found fixed large width. Needs `w-full md:w-[...]`.
- Line 336: Found fixed large height. Needs `h-auto md:h-[...]`.
- Line 337: Found fixed large width. Needs `w-full md:w-[...]`.
- Line 337: Found fixed large height. Needs `h-auto md:h-[...]`.
- Line 667: Found fixed large width. Needs `w-full md:w-[...]`.
- ... and 3 more similar layout issues.

### index11.html
- Line 630: Found fixed large width. Needs `w-full md:w-[...]`.
- Line 630: Found fixed large height. Needs `h-auto md:h-[...]`.
- Line 874: Found fixed large height. Needs `h-auto md:h-[...]`.
- Line 953: Found fixed large height. Needs `h-auto md:h-[...]`.
- Line 2080: Found fixed large width. Needs `w-full md:w-[...]`.

### payroll-engine.html
- Line 335: Found fixed large width. Needs `w-full md:w-[...]`.
- Line 335: Found fixed large height. Needs `h-auto md:h-[...]`.
- Line 336: Found fixed large width. Needs `w-full md:w-[...]`.
- Line 336: Found fixed large height. Needs `h-auto md:h-[...]`.
- Line 382: Found fixed large height. Needs `h-auto md:h-[...]`.
- ... and 1 more similar layout issues.

### platform.html
- Line 368: Found fixed large width. Needs `w-full md:w-[...]`.
- Line 368: Found fixed large height. Needs `h-auto md:h-[...]`.
- Line 369: Found fixed large width. Needs `w-full md:w-[...]`.
- Line 369: Found fixed large height. Needs `h-auto md:h-[...]`.
- Line 710: Found fixed large width. Needs `w-full md:w-[...]`.
- ... and 4 more similar layout issues.

### pricing.html
- Line 833: Found fixed large width. Needs `w-full md:w-[...]`.
- Line 982: Found fixed large width. Needs `w-full md:w-[...]`.
- Line 1172: Found fixed large width. Needs `w-full md:w-[...]`.

### pxp-guarantee.html
- Line 337: Found fixed large width. Needs `w-full md:w-[...]`.
- Line 337: Found fixed large height. Needs `h-auto md:h-[...]`.
- Line 382: Found fixed large width. Needs `w-full md:w-[...]`.
- Line 383: Found fixed large width. Needs `w-full md:w-[...]`.
- Line 565: Found fixed large width. Needs `w-full md:w-[...]`.

### team-chat.html
- Line 335: Found fixed large width. Needs `w-full md:w-[...]`.
- Line 335: Found fixed large height. Needs `h-auto md:h-[...]`.
- Line 336: Found fixed large width. Needs `w-full md:w-[...]`.
- Line 336: Found fixed large height. Needs `h-auto md:h-[...]`.
- Line 417: Potential flex-row issue on mobile.
- ... and 1 more similar layout issues.

### workforce-os.html
- Line 634: Found fixed large height. Needs `h-auto md:h-[...]`.
- Line 1671: Found fixed large width. Needs `w-full md:w-[...]`.
- Line 1671: Found fixed large height. Needs `h-auto md:h-[...]`.
- Line 1794: Found fixed large width. Needs `w-full md:w-[...]`.
- Line 1794: Found fixed large height. Needs `h-auto md:h-[...]`.
- ... and 3 more similar layout issues.

## Verification Plan

- Inspect each page using Chrome DevTools device toolbar (Mobile view - 375px/414px width).
- Ensure no horizontal scrolling occurs.
- Ensure flex layouts stack correctly.
- Ensure font sizes scale down properly on small screens (using `text-3xl md:text-5xl`).
